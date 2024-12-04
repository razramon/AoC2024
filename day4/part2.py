from pathlib import Path
import time
import re

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def search(mat, x, y):
    directions = [[[-1, -1], [0, 0], [1, 1]], [[1, -1], [0, 0], [-1, 1]]]
    for dir in directions:
        curr = ["S", "A", "M"]
        for i, j in dir:
            i_x = x + i
            i_y = y + j
            if (
                not (0 <= i_x < len(mat) and 0 <= i_y < len(mat[0]))
                or mat[i_x][i_y] not in curr
            ):
                return 0
            curr.pop(curr.index(mat[i_x][i_y]))
    return 1


def question(content):
    ans = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] == "A":
                ans += search(content, i, j)
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
