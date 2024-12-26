from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def update_mat(mat, pos, move):
    x = pos[0] + move[0]
    y = pos[1] + move[1]
    if mat[x][y] == "#":
        return pos
    elif mat[x][y] == ".":
        mat[pos[0]][pos[1]] = "."
        mat[x][y] = "@"
    elif mat[x][y] in "[]":
        if move[0] == 0:  # left or right moves
            while mat[x][y] not in ".#":
                x += move[0]
                y += move[1]
            if mat[x][y] == "#":
                return pos
            if mat[x][y] == ".":
                while x != (pos[0] + move[0]) or y != (pos[1] + move[1]):
                    mat[x][y] = mat[x - move[0]][y - move[1]]
                    x -= move[0]
                    y -= move[1]
                mat[x][y] = "@"
                mat[pos[0]][pos[1]] = "."
        else:  # up and down moves
            stack = [[x, y]]
            if mat[x][y] == "]":
                stack.append([x, y - 1])
            elif mat[x][y] == "[":
                stack.append([x, y + 1])

            seen = set()
            bad_cell = False
            while stack:
                i, j = stack.pop()
                n_i = i + move[0]
                n_j = j + move[1]
                if mat[n_i][n_j] == "#":
                    bad_cell = True
                    break
                if (i, j) in seen:
                    continue

                seen.add((i, j))
                if mat[n_i][n_j] == "]":
                    stack.append([n_i, n_j])
                    stack.append([n_i, n_j - 1])
                elif mat[n_i][n_j] == "[":
                    stack.append([n_i, n_j])
                    stack.append([n_i, n_j + 1])
            if bad_cell:
                return pos
            rev = True
            if move[0] == -1:
                rev = False
            seen = sorted(list(seen), key=lambda x: x[0], reverse=rev)
            for i, j in seen:
                mat[i + move[0]][j + move[1]] = mat[i][j]
                mat[i][j] = "."
            mat[pos[0]][pos[1]] = "."
            mat[x][y] = "@"
    return [x, y]


def get_start_pos(mat):
    for i, line in enumerate(mat):
        for j, c in enumerate(line):
            if c == "@":
                return [i, j]


def get_coordinates(mat):
    ans = 0
    for i, line in enumerate(mat):
        for j, c in enumerate(line):
            if c == "[":
                ans += i * 100 + j
    return ans


def print_mat(mat):
    for line in mat:
        print("".join(line))
    print("-" * 100)


def question(mat, move):
    pos = get_start_pos(mat)
    for m in move:
        if m == "<":
            pos = update_mat(mat, pos, [0, -1])
        elif m == ">":
            pos = update_mat(mat, pos, [0, 1])
        elif m == "^":
            pos = update_mat(mat, pos, [-1, 0])
        elif m == "v":
            pos = update_mat(mat, pos, [1, 0])
    return get_coordinates(mat)


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    mat = []
    for i, line in enumerate(content):
        if len(line) == 0:
            break
        curr = []
        for s in line:
            if s == "#":
                curr.append("#")
                curr.append("#")
            elif s == ".":
                curr.append(".")
                curr.append(".")
            elif s == "O":
                curr.append("[")
                curr.append("]")
            elif s == "@":
                curr.append("@")
                curr.append(".")
        mat.append(curr)
    movement = []
    for j in range(i + 1, len(content)):
        for s in content[j]:
            movement.append(s)
    print(question(mat, movement))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
