from pathlib import Path
import time
from itertools import permutations, product
from functools import lru_cache

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

keyboards = [
    [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]],
    [[None, "^", "A"], ["<", "v", ">"]],
]
maping = {(-1, 0): "^", (1, 0): "v", (0, -1): "<", (0, 1): ">"}


def get_pos(mat, key):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == key:
                return [i, j]


@lru_cache(None)
def dfs(key, start, finish):
    mat = keyboards[key]
    start_i = get_pos(mat, start)
    end_i = get_pos(mat, finish)
    path = []
    # left right
    curr = start_i[0]
    while curr > end_i[0]:
        curr -= 1
        path.append([-1, 0])
    while curr < end_i[0]:
        curr += 1
        path.append([1, 0])

    # up down
    curr = start_i[1]
    while curr > end_i[1]:
        curr -= 1
        path.append([0, -1])
    while curr < end_i[1]:
        curr += 1
        path.append([0, 1])
    all_paths = permutations(path)
    good_paths = set()

    for p in all_paths:
        good = True
        i, j = start_i[0], start_i[1]
        for dir in p:
            i += dir[0]
            j += dir[1]
            if mat[i][j] == None:
                good = False
                break
        if good:
            out = []
            for i in range(len(p)):
                out += maping[(p[i][0], p[i][1])]
            out += ["A"]
            good_paths.add("".join(out))
    return list(good_paths)


@lru_cache(None)
def get_path(key, prev, curr, depth=0):
    if depth == 0:
        return len(min(dfs(key, prev, curr), key=len))

    best = float("inf")
    p = dfs(key, prev, curr)
    for seq in p:
        seq = "A" + seq
        curr = 0
        for i in range(len(seq) - 1):
            curr += get_path(1, seq[i], seq[i + 1], depth - 1)
        best = min(curr, best)

    return best


def question(content):
    total_dept = 25
    ans = 0
    for line in content:
        curr = "A" + line
        line_ans = 0
        for i in range(len(curr) - 1):
            line_ans += get_path(0, curr[i], curr[i + 1], total_dept)
        ans += line_ans * int(line[:-1])
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    print(question(content))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
