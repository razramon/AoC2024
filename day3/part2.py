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


def get_do_mult(content):
    dont_split = content.split("don't()")
    do_split = [dont_split[0]]
    for x in dont_split:
        if "do()" in x:
            do_split += x.split("do()")[1:]
    ans = 0
    for part in do_split:
        ans += question(part)
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read()

    print(get_do_mult(content))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
