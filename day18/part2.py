from pathlib import Path
import time
from collections import defaultdict
import heapq
import numpy as np

SCRIPT_DIR = Path(__file__).parent

TEST = True
if TEST:
    file = "test.txt"
    max_ = 7
    k = 12
else:
    file = "input.txt"
    max_ = 71
    k = 1024

INPUT_FILE = Path(SCRIPT_DIR, file)
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dijkstra(mat):
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
            return True

        for dir in directions:
            x = i + dir[0]
            y = j + dir[1]
            if 0 <= x < n and 0 <= y < n and [x, y] != [parent_i, parent_j]:
                heapq.heappush(heap, (curr_cost + 1, x, y, i, j))
    return False


def print_mat(mat):
    for line in mat:
        print("".join(line))
    print()


def question(mat, bytes):
    left = 0
    right = len(bytes) - 1
    while left <= right:
        curr = np.copy(mat)
        mid = (left + right) // 2
        for l in range(mid):
            i, j = bytes[l]
            curr[i][j] = "#"
        if dijkstra(curr):
            left = mid + 1
        else:
            right = mid - 1
    return bytes[right]


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    for i in range(len(content)):
        content[i] = [int(x) for x in content[i].split(",")]
    mat = [["."] * max_ for _ in range(max_)]
    mat = np.array(mat)
    l = 0
    for i, j in content:
        mat[i][j] = "#"
        l += 1
        if l == k:
            break

    print(question(mat, content[k:]))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
