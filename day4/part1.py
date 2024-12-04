from pathlib import Path
import time
import re

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def search(mat, x, y):
    ans = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            found = True
            for k, letter in enumerate("XMAS"):
                i_x = x + i * k
                i_y = y + j * k
                if (
                    not (0 <= i_x < len(mat) and 0 <= i_y < len(mat[0]))
                    or mat[x + i * k][y + j * k] != letter
                ):
                    found = False
                    break
            if found:
                ans += 1
    return ans


def question(content):
    ans = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] == "X":
                ans += search(content, i, j)
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.readlines()
    print(question(content))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
