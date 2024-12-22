from pathlib import Path
import time
from collections import Counter, deque
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def get_start_pos(mat):
    start = None
    path_len = 0
    for i, line in enumerate(mat):
        for j, c in enumerate(line):
            if c == "S":
                start = [i, j]
            if c != "#":
                path_len += 1
    return start, path_len


def print_mat(mat, path):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if [i, j] in path:
                print(colored(mat[i][j], "red"), end="")
            else:
                print(mat[i][j], end="")
        print()
    print("-" * 100)


def get_all_paths(mat, start, path_len):
    path = [[start, 0]]
    path_index = [start]
    curr = start
    before = start
    for i in range(path_len):
        for dir in directions:
            x = curr[0] + dir[0]
            y = curr[1] + dir[1]
            if mat[x][y] != "#" and [x, y] != before:
                path.append([[x, y], path_len - i])
                path_index.append([x, y])
                break
        before = curr
        curr = [x, y]
    return path, path_index


def question(mat):
    start, path_len = get_start_pos(mat)
    path, _ = get_all_paths(mat, start, path_len)
    saved = []
    for i in range(len(path)):
        i_x, i_y = path[i][0]
        for j in range(i + 1, len(path)):
            j_x, j_y = path[j][0]
            score_j = path[j][1]
            if abs(i_x - j_x) + abs(i_y - j_y) <= 20:
                saved.append(
                    path_len + 1 - (i + score_j + abs(i_x - j_x) + abs(i_y - j_y))
                )
    counter = Counter(saved)
    return sum([counter[x] for x in counter if x >= 100])


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
