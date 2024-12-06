from pathlib import Path
import time
import re
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def question(mat, x, y):
    n = len(mat)
    ans = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dir_idx = 0
    while 0 <= x < n and 0 <= y < n:
        if mat[x][y] == "." or mat[x][y] == "^":
            mat[x][y] = "0"
            ans += 1
            x += directions[dir_idx][0]
            y += directions[dir_idx][1]
        elif mat[x][y] == "0":
            x += directions[dir_idx][0]
            y += directions[dir_idx][1]
        elif mat[x][y] == "#":
            x -= directions[dir_idx][0]
            y -= directions[dir_idx][1]
            dir_idx = (dir_idx + 1) % len(directions)
            x += directions[dir_idx][0]
            y += directions[dir_idx][1]
        # print_mat(mat)
    return ans


def print_mat(mat):
    for line in mat:
        print(line)
    print("-" * 10)


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    for i in range(len(content)):
        content[i] = list(content[i])
    x = 0
    y = 0
    found = False
    for i, line in enumerate(content):
        for j, letter in enumerate(line):
            if letter == "^":
                x, y = i, j
                found = True
                break
        if found:
            break

    print(question(content, x, y))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
