from pathlib import Path
import time
import re
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def question(updates, before, after):
    ans = 0
    for update in updates:
        update = update.split(",")
        found = True
        for i in range(len(update)):
            if update[i] not in before or update[i] not in after:
                continue
            for j in range(i):
                if update[j] not in before[update[j]]:
                    continue
                if update[j] not in before[update[i]]:
                    found = False
                    break
            if not found:
                break
            for j in range(i + 1, len(update)):
                if update[j] not in after:
                    continue
                if update[j] not in after[update[i]]:
                    found = False
                    break

        if found:
            ans += int(update[len(update) // 2])

    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    before_order = defaultdict(list)
    after_order = defaultdict(list)
    for i, line in enumerate(content):
        if line == "":
            break
        line = line.split("|")
        before_order[line[1]].append(line[0])
        after_order[line[0]].append(line[1])
    print(question(content[i + 1 :], before_order, after_order))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
