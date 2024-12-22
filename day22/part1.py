from pathlib import Path
import time

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
    ans = 0
    for line in content:
        secret = line
        for _ in range(2000):
            secret = process(secret)
        ans += secret
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    print(question([int(x) for x in content]))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
