from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


# dynamic programming
def check_possible(p, comb):
    n = len(p)
    dp = [False] * n
    for i in range(n):
        if p[: i + 1] in comb:
            dp[i] = True
            continue

        for c in comb:
            if p[i - len(c) + 1 : i + 1] == c and dp[i - len(c)]:
                dp[i] = True
                break

    return dp[-1]


def question(comb, poss):
    ans = 0
    for p in poss:
        ans += check_possible(p, comb)
    print(ans)


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    comb = content[0].split(", ")
    question(comb, content[2:])


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
