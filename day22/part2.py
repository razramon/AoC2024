from pathlib import Path
import time
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def mix(a, b):
    return a ^ b


def prune(secret):
    return secret % 16777216


def process(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret


def question(content):
    sums = defaultdict(int)
    for line in content:
        updated = set()
        curr = []
        secret = line
        for _ in range(2000):
            next_secret = process(secret)
            if len(curr) < 4:
                curr.append(next_secret % 10 - secret % 10)
            else:
                if (curr[0], curr[1], curr[2], curr[3]) not in updated:
                    sums[(curr[0], curr[1], curr[2], curr[3])] += secret % 10
                    updated.add((curr[0], curr[1], curr[2], curr[3]))
                curr.pop(0)
                curr.append(next_secret % 10 - secret % 10)
            secret = next_secret
    return max(sums.values())


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    print(question([int(x) for x in content]))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
