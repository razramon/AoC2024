from pathlib import Path
import time
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


class Computer:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def get_combo_operand(self, op):  # operand
        if 0 <= op <= 3:
            return op
        if op == 4:
            return self.A
        if op == 5:
            return self.B
        if op == 6:
            return self.C

    def get_instuctions(self, opcode, operand):
        if opcode == 0:
            self.A = int(self.A / 2 ** self.get_combo_operand(operand))
        if opcode == 1:
            self.B ^= operand
        if opcode == 2:
            self.B = self.get_combo_operand(operand) % 8
        if opcode == 3:
            if self.A != 0:
                return operand
        if opcode == 4:
            self.B ^= self.C
        if opcode == 5:
            return self.get_combo_operand(operand) % 8
        if opcode == 6:
            self.B = int(self.A / 2 ** self.get_combo_operand(operand))
        if opcode == 7:
            self.C = int(self.A / 2 ** self.get_combo_operand(operand))
        return -1


def compute_output(a, p, program):
    output = []
    a <<= 3
    for x in range(a, a + 8):
        comp = Computer(x, 0, 0)
        for i in range(0, len(program) - 1, 2):
            if program[i] == 5:
                out = comp.get_instuctions(program[i], program[i + 1])
                if out == p:
                    output.append(x)
                break
            else:
                comp.get_instuctions(program[i], program[i + 1])
    return output


def question(program):
    A = [0]
    for p in program[::-1]:
        A = sum([compute_output(a, p, program) for a in A], [])
    return min(A)


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    A = int(content[0].split()[-1])
    B = int(content[1].split()[-1])
    C = int(content[2].split()[-1])
    comp = Computer(A, B, C)
    program = [int(x) for x in content[4].split()[-1].split(",")]

    print(question(program))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
