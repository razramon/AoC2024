from pathlib import Path
import time
import re
from collections import defaultdict, deque

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def get_trails(mat, x, y):
    queue = deque([[x, y]])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    ans = set()
    while queue:
        i, j = queue.popleft()
        curr = int(mat[i][j])
        for dir in directions:
            new_i, new_j = i + dir[0], j + dir[1]
            if 0 <= new_i < len(mat) and 0 <= new_j < len(mat[0]):
                if int(mat[new_i][new_j]) - 1 == curr:
                    if int(mat[new_i][new_j]) == 9:
                        ans.add((new_i, new_j))
                    else:
                        queue.append([new_i, new_j])
    return len(ans)


def question(mat):
    ans = 0
    for i, line in enumerate(mat):
        for j, s in enumerate(line):
            if s == "0":
                ans += get_trails(mat, i, j)

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
