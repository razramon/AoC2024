from pathlib import Path
import time
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def question(locks, keys):
    ans = 0
    for lock in locks:
        for key in keys:
            curr = [x + y for x, y in zip(lock, key)]
            if all([x <= 5 for x in curr]):
                ans += 1
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    keys = []
    locks = []
    curr = []
    for k, line in enumerate(content):
        if len(line) == 0 or k == len(content) - 1:
            pins = []
            for j in range(5):  # number of pins
                pins.append(0)
                for i in range(1, len(curr) - 1):
                    pins[-1] += 1 if curr[i][j] == "#" else 0
            if curr[0] == "#####":
                locks.append(pins)
            else:
                keys.append(pins)
            curr = []
        else:
            curr.append(line)
    print(question(locks, keys))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
