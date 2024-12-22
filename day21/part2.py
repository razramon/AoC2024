from pathlib import Path
import time
from itertools import permutations, product
from functools import lru_cache
SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "test.txt")

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

def dfs(mat, start, finish):
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

def get_path(key, seq):
    key1 = keyboards[key]
    prev = seq.pop(0)
    path = []
    while seq:
        curr = seq.pop(0)
        p = dfs(key1, prev, curr)
        path.append(p)
        prev = curr
    return ["".join(x) for x in product(*path)]


def question(content):
    keys = [0] + [1] * 2
    ans = 0
    for line in content:
        curr = ["A"]+list(line)
        line_ans = 0
        total_line = []
        for i in range(len(curr) -1):
            seq = [[curr[i],curr[i+1]]]
            print(seq)
            for j in range(len(keys)):
                next = []
                for poss in seq:
                    poss = ["A"] + list(poss)
                    next.extend(get_path(keys[j], poss))
                seq = list(set(next))
            seq = min(seq, key=len)
            total_line.append(seq)
            print(seq)
            line_ans += (len(seq))
        print("".join(total_line))
        print(line_ans, int(line[:-1]))
        ans += line_ans * int(line[:-1])
        break
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
