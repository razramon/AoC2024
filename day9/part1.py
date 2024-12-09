from pathlib import Path
import time
import re
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def checksum(arr):
    ans = 0
    idx = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != ".":
                ans += idx * arr[i][j]
            idx += 1
    return ans


def change_order(arr):
    j = len(arr) - 1
    if arr[j][0] == ".":
        j -= 1
    left = []
    for i in range(1, len(arr), 2):
        if i > j + 2:
            break
        while len(left) < len(arr[i]):
            left += arr[j]
            arr[j] = "." * len(arr[j])
            j -= 2
        arr[i] = left[: len(arr[i])]
        left = left[len(arr[i]) :]
    if len(left) > 0:
        arr[j + 2] = left + ["."] * (len(arr[j + 2]) - len(left))
    return arr


def question(content):
    arr = []
    j = 0
    for i, s in enumerate(content):
        if i % 2 == 0:
            arr.append([j] * int(s))
            j += 1
        else:
            arr.append("." * int(s))
    return checksum(change_order(arr))


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().strip()
    print(question(content))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
