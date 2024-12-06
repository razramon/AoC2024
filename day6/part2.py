from pathlib import Path
import time
import re
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def test_mat(mat, x, y, dir_idx):
    n = len(mat)
    seen = []
    while 0 <= x < n and 0 <= y < n:
        if mat[x][y] == "." or mat[x][y] == "^":
            x += directions[dir_idx][0]
            y += directions[dir_idx][1]
        elif mat[x][y] == "0":
            x += directions[dir_idx][0]
            y += directions[dir_idx][1]
        elif mat[x][y] == "#":
            if (x, y, dir_idx) in seen:
                return 1
            seen.append((x, y, dir_idx))
            x -= directions[dir_idx][0]
            y -= directions[dir_idx][1]
            dir_idx = (dir_idx + 1) % len(directions)
            x += directions[dir_idx][0]
            y += directions[dir_idx][1]
    return 0


def question(mat, x, y):
    ans = 0
    n = len(mat)
    dir_idx = 0

    while 0 <= x < n and 0 <= y < n:
        if mat[x][y] == "." or mat[x][y] == "^":
            if mat[x][y] == ".":
                mat[x][y] = "#"
                ans += test_mat(mat, x, y, dir_idx)
            mat[x][y] = "0"
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
