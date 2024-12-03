from pathlib import Path
import time
import re

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def get_mult(match):
    match = match.replace("mul(", "")
    match = match.replace(")", "")
    match = [int(x) for x in match.split(",")]
    return match[0] * match[1]


def question(content):
    ans = 0
    pattern = "mul\(\d+,\d+\)"
    matches = re.findall(pattern, content)
    for match in matches:
        ans += get_mult(match)
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read()

    print(question(content))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
