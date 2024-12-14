from pathlib import Path
import time
import os

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

width = 101
length = 103
num_sec = 1000


def print_board(robots, counter):
    board = [[" " for _ in range(width)] for _ in range(length)]

    for robot in robots:
        y, x = robot[0]
        board[x][y] = "#"
    to_show = False
    for line in board:
        # check if at least 7 in a row
        if "#######" in "".join(line):
            to_show = True
            break
    if to_show:
        print(counter)
        for line in board:
            print("".join(line))
        print("-" * 101)
        q = input()
        if q == "q":
            exit()
        os.system("cls")


def get_position(robot):
    x = robot[0][0]
    y = robot[0][1]
    x = (x + robot[1][0]) % width
    y = (y + robot[1][1]) % length
    return [x, y]


def question(robots):
    counter = 0
    while True:
        for _ in range(width * length):
            counter += 1
            for i, robot in enumerate(robots):
                robots[i][0] = get_position(robot)
            print_board(robots, counter)


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    robots = []
    for line in content:
        line = line.split()
        line[0] = [int(x) for x in line[0].split("=")[1].split(",")]
        line[1] = [int(x) for x in line[1].split("=")[1].split(",")]
        robots.append(line)
    question(robots)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
