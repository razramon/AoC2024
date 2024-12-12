from pathlib import Path
import time
from collections import deque

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def get_area(mat, x, y):
    sym = mat[x][y]
    seen = set()
    perimeter = 0
    queue = deque([[x, y]])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while queue:
        i, j = queue.popleft()
        if (i, j) not in seen:
            seen.add((i, j))
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if (
                    0 <= new_i < len(mat)
                    and 0 <= new_j < len(mat[0])
                    and mat[new_i][new_j] == sym
                ):
                    queue.append([new_i, new_j])
                else:
                    perimeter += 1
    return seen, perimeter


def question(mat):
    ans = 0
    seen = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if (i, j) not in seen:
                area, perimeter = get_area(mat, i, j)
                seen += list(area)
                ans += len(area) * perimeter
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    print(question(content))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
