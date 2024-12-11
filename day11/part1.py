from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def generate_stones(stone):
    stones = [stone]
    for i in range(25):
        new_stones = []
        for s in stones:
            if s == "0":
                new_stones.append("1")
            elif len(s) % 2 == 0:
                new_stones.append(str(int(s[: len(s) // 2])))
                new_stones.append(str(int(s[len(s) // 2 :])))
            else:
                new_stones.append(str(int(s) * 2024))
        stones = new_stones
    return len(stones)


def question(content):
    ans = 0
    for stone in content.split():
        ans += generate_stones(stone)

    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().strip()
    print(question(content))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
