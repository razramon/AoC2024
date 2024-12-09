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
    i = 1
    while i < len(arr):
        if len(arr[i]) == 0 or arr[i][0] != ".":
            i += 1
            continue
        j = len(arr) - 1
        while len(arr[j]) > len(arr[i]) or type(arr[j]) != list or len(arr[j]) == 0:
            j -= 1
        if j <= i:
            i += 1
            continue
        left = len(arr[i]) - len(arr[j])
        arr[i], arr[j] = arr[j], arr[i][: len(arr[j])]
        if left > 0:
            arr.insert(i + 1, "." * left)
        i += 1
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
