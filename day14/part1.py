from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

width = 101
length = 103
num_sec = 100


def get_position(robot):
    x = robot[0][0]
    y = robot[0][1]
    for _ in range(num_sec):
        x = (x + robot[1][0]) % width
        y = (y + robot[1][1]) % length
    return x, y


def question(robots):
    quad = [0] * 4
    for robot in robots:
        pos = get_position(robot)
        if pos[0] == width // 2 or pos[1] == length // 2:
            continue
        if pos[0] < width // 2 and pos[1] < length // 2:
            quad[0] += 1
        elif pos[0] < width // 2 and pos[1] > length // 2:
            quad[1] += 1
        elif pos[0] > width // 2 and pos[1] > length // 2:
            quad[2] += 1
        else:
            quad[3] += 1
    ans = 1
    for x in quad:
        ans *= x
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    robots = []
    for line in content:
        line = line.split()
        line[0] = [int(x) for x in line[0].split("=")[1].split(",")]
        line[1] = [int(x) for x in line[1].split("=")[1].split(",")]
        robots.append(line)
    print(question(robots))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
