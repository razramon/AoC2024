from pathlib import Path
import time
from collections import deque, defaultdict
from copy import deepcopy
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up down  # left right


def get_start_pos(mat):
    for i, line in enumerate(mat):
        for j, c in enumerate(line):
            if c == "S":
                return [i, j]


class Way:
    def __init__(self, x, y, dir, score=0):
        self.x = x
        self.y = y
        self.score = score
        self.dir = dir
        self.path = [[x, y]]

    def walk(self, dir):
        if dir != self.dir:
            self.score += 1001
        else:
            self.score += 1
        self.dir = dir
        self.x += dir[0]
        self.y += dir[1]
        self.path.append([self.x, self.y])

    def get_score(self, dir):
        if dir != self.dir:
            return self.score + 1001
        else:
            return self.score + 1


def print_mat(mat, path):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if [i, j] in path:
                print(colored(mat[i][j], "red"), end="")
            else:
                print(mat[i][j], end="")
        print()
    print("-" * 100)


def question(mat):
    start = get_start_pos(mat)
    queue = deque()
    reached = []
    w = Way(start[0], start[1], [0, 1])
    queue.append(w)
    seen = defaultdict(int)
    while queue:
        w = queue.popleft()
        for dir in directions:
            x = w.x + dir[0]
            y = w.y + dir[1]
            if seen[(x, y)] != 0 and w.get_score(dir) >= seen[(x, y)]:
                continue
            seen[(x, y)] = w.get_score(dir)
            if mat[x][y] == "E":
                w.walk(dir)
                reached.append(w)
            if mat[x][y] == ".":
                new_w = Way(w.x, w.y, w.dir, w.score)
                # new_w = deepcopy(w) slow!!!!!!!!!
                new_w.walk(dir)
                queue.append(new_w)
    return min([w.score for w in reached])


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
