from pathlib import Path
import time
import re
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def check_distance(a, b):
    loc = []
    dist_x = abs(a[0] - b[0])
    if a[0] > b[0]:
        dist_x *= -1
    loc.append([a[0] - dist_x])
    loc.append([b[0] + dist_x])

    dist_y = abs(a[1] - b[1])
    if a[1] > b[1]:
        dist_y *= -1
    loc[0].append(a[1] - dist_y)
    loc[1].append(b[1] + dist_y)

    return loc


def question(locations, length, width):
    antinodes = set()
    for antenna in locations:
        places = locations[antenna]
        for i in range(len(places)):
            for j in range(i + 1, len(places)):
                temp = check_distance(places[i], places[j])
                for loc in temp:
                    if 0 <= loc[0] < width and 0 <= loc[1] < length:
                        antinodes.add((loc[0], loc[1]))
    return len(antinodes)


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()

    loc = defaultdict(list)
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] != ".":
                loc[content[i][j]].append([i, j])
    print(question(loc, len(content), len(content[0])))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
