from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "test.txt")


def update_mat(mat, pos, move):
    x = pos[0] + move[0]
    y = pos[1] + move[1]
    if mat[x][y] == "#":
        return pos
    elif mat[x][y] == ".":
        mat[pos[0]][pos[1]] = "."
        mat[x][y] = "@"
    elif mat[x][y] in "[]":
        if(move[0] == 0): #left or right moves
            while mat[x][y] not in ".#":
                x += move[0]
                y += move[1]
            if mat[x][y] == "#":
                return pos
            if mat[x][y] == ".":
                while x != (pos[0] + move[0]) or y != (pos[1] + move[1]):
                    mat[x][y] = mat[x-move[0]][y-move[1]]
                    x -= move[0]
                    y -= move[1]
                mat[x][y] = "@"
                mat[pos[0]][pos[1]] = "."
        else: # up and down moves
            print("here")
            to_check = []
            if(mat[x][y] == "]"):
                to_check.append([y,y+1])
            else:
                to_check.append([y-1,y])
            next_floor = []
            for i in range(len(mat)):
                bad_cell = False
                x += move[0]
                curr = to_check[-1]
                if(all(mat[x][curr[0]:curr[1]+1]) == "."):
                    break
                for j in range(curr[0], curr[1] + 1):
                    if(mat[x][j] == "]" and j == curr[0]):
                        next_floor.append(j - 1)
                    if(mat[x][j] == "#"):
                        bad_cell = True
                        break
                    if(mat[x][j] == "[" and j == curr[1]):
                        next_floor.append(j+1)
                if(bad_cell):
                    break
                to_check.append(next_floor)
            print(to_check)

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
    print_mat(mat)
    for m in move:
        print(m)
        if m == "<":
            pos = update_mat(mat, pos, [0, -1])
        elif m == ">":
            pos = update_mat(mat, pos, [0, 1])
        elif m == "^":
            pos = update_mat(mat, pos, [-1, 0])
        elif m == "v":
            pos = update_mat(mat, pos, [1, 0])
        print_mat(mat)
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
            if(s == "#"):
                curr.append("#")
                curr.append("#")
            elif(s== "."):
                curr.append(".")
                curr.append(".")
            elif(s == "O"):
                curr.append("[")
                curr.append("]")
            elif(s == "@"):
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
