from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def check_safty(line):
    sorted_line = sorted(line)
    if sorted_line != line and sorted_line[::-1] != line:
        return False
    for i in range(1, len(line)):
        if not (1 <= abs(line[i] - line[i - 1]) <= 3):
            return False
    return True


def question(lines):
    ans = 0
    for line_input in lines:
        if check_safty(line_input):
            ans += 1
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        lines = f.readlines()
    content = []
    for line in lines:
        content.append([int(x) for x in line.strip().split(" ")])

    print(question(content))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
