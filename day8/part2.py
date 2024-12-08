from pathlib import Path
import time
import re
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def check_distance(a, b, length, width):
    loc_a = []
    loc_b = []
    dist_x = abs(a[0] - b[0])
    if a[0] > b[0]:
        i = 1
        while 0 <= a[0] + dist_x * i < length:
            loc_a.append([a[0] + dist_x * i])
            i += 1
        i = 1
        while 0 <= b[0] - dist_x * i < length:
            loc_b.append([b[0] - dist_x * i])
            i += 1
    else:
        i = 1
        while 0 <= a[0] - dist_x * i < length:
            loc_a.append([a[0] - dist_x * i])
            i += 1
        i = 1
        while 0 <= b[0] + dist_x * i < length:
            loc_b.append([b[0] + dist_x * i])
            i += 1

    dist_y = abs(a[1] - b[1])
    if a[1] > b[1]:
        for i in range(len(loc_a)):
            loc_a[i].append(a[1] + dist_y * (i + 1))

        for i in range(len(loc_b)):
            loc_b[i].append(b[1] - dist_y * (i + 1))

    else:
        for i in range(len(loc_a)):
            loc_a[i].append(a[1] - dist_y * (i + 1))

        for i in range(len(loc_b)):
            loc_b[i].append(b[1] + dist_y * (i + 1))

    return loc_a + loc_b


def question(locations, length, width):
    antinodes = set()
    for antenna in locations:
        places = locations[antenna]
        for i in range(len(places)):
            antinodes.add((places[i][0], places[i][1]))
            for j in range(i + 1, len(places)):
                temp = check_distance(places[i], places[j], length, width)
                for loc in temp:
                    if 0 <= loc[0] < length and 0 <= loc[1] < width:
                        antinodes.add((loc[0], loc[1]))
    # print_board(locations, antinodes, length, width)
    return len(antinodes)


def print_board(locations, antinodes, length, width):
    board = [["." for _ in range(width)] for _ in range(length)]
    for antenna in locations:
        for loc in locations[antenna]:
            board[loc[0]][loc[1]] = antenna
    for x, y in antinodes:
        if board[x][y] == ".":
            board[x][y] = "#"
    for line in board:
        print("".join(line))


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
