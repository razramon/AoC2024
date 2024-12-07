from pathlib import Path
import time
import re
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def check_eval(line):
    ans = line[0]
    vars = line[1]
    possibilities = [vars[0] * vars[1], vars[0] + vars[1]]
    for i in range(2, len(vars)):
        temp = []
        for j in range(len(possibilities)):
            temp.append(possibilities[j] + vars[i])
            temp.append(possibilities[j] * vars[i])
        possibilities = temp
    return ans in possibilities


def question(lines):
    ans = 0
    for line in lines:
        if check_eval(line):
            ans += line[0]
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    for i in range(len(content)):
        content[i] = content[i].split(": ")
        content[i][0] = int(content[i][0])
        content[i][1] = [int(x) for x in content[i][1].split()]

    print(question(content))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
