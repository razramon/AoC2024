from pathlib import Path
import time
from collections import deque, defaultdict
from termcolor import colored
import heapq

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def get_start_pos(mat):
    start, end = None, None
    for i, line in enumerate(mat):
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)
            if c == "E":
                end = (i, j)
    return start, end


# Dijkstra
def question(mat):
    start, end = get_start_pos(mat)
    heap = [(0, 0, *start, 0, *start)]
    cost = {}
    deps = defaultdict(list)
    end_direction = 0
    while len(heap) > 0:
        curr_cost, curr_dir, i, j, paret_dir, parent_i, parent_j = heapq.heappop(heap)

        if (curr_dir, i, j) in cost:
            if cost[(curr_dir, i, j)] == curr_cost:
                deps[(curr_dir, i, j)].append((paret_dir, parent_i, parent_j))
            continue

        deps[(curr_dir, i, j)].append((paret_dir, parent_i, parent_j))
        cost[(curr_dir, i, j)] = curr_cost

        if mat[i][j] == "#":
            continue

        if mat[i][j] == "E":
            end_direction = curr_dir
            # print(curr_cost)
            break

        x = i + directions[curr_dir][0]
        y = j + directions[curr_dir][1]

        heapq.heappush(heap, (curr_cost + 1, curr_dir, x, y, curr_dir, i, j))
        # split
        heapq.heappush(
            heap, (curr_cost + 1000, (curr_dir + 1) % 4, i, j, curr_dir, i, j)
        )
        heapq.heappush(
            heap, (curr_cost + 1000, (curr_dir + 3) % 4, i, j, curr_dir, i, j)
        )

    stack = [(end_direction, *end)]
    seen = set()
    seen_pos = set()
    while len(stack) > 0:
        curr = stack.pop()
        if curr in seen:
            continue

        seen.add(curr)
        seen_pos.add(curr[1:])

        for neighbor in deps[curr]:
            stack.append(neighbor)

    return len(seen_pos)


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    mat = []
    for i, line in enumerate(content):
        if len(line) == 0:
            break
        mat.append(list(line))
    print(question(mat))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
