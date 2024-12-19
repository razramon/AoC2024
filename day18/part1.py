from pathlib import Path
import time
from collections import defaultdict
import heapq

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# Dijkstra
def question(mat):
    n = len(mat)
    start, end = (0, 0), (n - 1, n - 1)
    heap = [(0, *start, *start)]
    cost = {}
    deps = defaultdict(list)
    while len(heap) > 0:
        curr_cost, i, j, parent_i, parent_j = heapq.heappop(heap)

        if (i, j) in cost:
            if cost[(i, j)] == curr_cost:
                deps[(i, j)].append((parent_i, parent_j))
            continue

        deps[(i, j)].append((parent_i, parent_j))
        cost[(i, j)] = curr_cost

        if mat[i][j] == "#":
            continue

        if (i, j) == end:
            print(curr_cost)
            break

        for dir in directions:
            x = i + dir[0]
            y = j + dir[1]
            if 0 <= x < n and 0 <= y < n and [x, y] != [parent_i, parent_j]:
                heapq.heappush(heap, (curr_cost + 1, x, y, i, j))

    return curr_cost


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    for i in range(len(content)):
        content[i] = [int(x) for x in content[i].split(",")]
    max_ = max(max(content)) + 1
    mat = [["."] * max_ for _ in range(max_)]
    k = 0
    for i, j in content:
        mat[i][j] = "#"
        k += 1
        if k == 1024:
            break
    for line in mat:
        print("".join(line))
    print(question(mat))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
