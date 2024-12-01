from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    with open(INPUT_FILE, mode="rt") as f:
        lines = f.readlines()
    left = []
    right = []
    for line in lines:
        curr = line.strip().split("   ")
        left.append(int(curr[0]))
        right.append(int(curr[1]))

    left = sorted(left)
    right = sorted(right)

    sum = 0
    for i in range(len(left)):
        sum += abs(right[i] - left[i])

    print(sum)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
