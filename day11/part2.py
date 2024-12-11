from pathlib import Path
import time
from tqdm import *
from collections import Counter, defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def generate_stones(s):
    new_stones = []
    if s == "0":
        new_stones.append("1")
    elif len(s) % 2 == 0:
        new_stones.append(str(int(s[: len(s) // 2])))
        new_stones.append(str(int(s[len(s) // 2 :])))
    else:
        new_stones.append(str(int(s) * 2024))
    return new_stones


def question(content):
    stones = Counter(content.split())
    for _ in range(75):
        next_stones = defaultdict(int)
        for stone in stones:
            for x in generate_stones(stone):
                next_stones[x] += stones[stone]

        stones = next_stones

    return sum(stones.values())


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().strip()
    print(question(content))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
