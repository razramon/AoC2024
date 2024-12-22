from pathlib import Path
import time
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "test.txt")


class Computer:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def get_combo_operand(self, op): # operand
        if(0<=op<=3):
            return op
        if(op == 4):
            return self.A
        if(op == 5):
            return self.B
        if(op == 6):
            return self.C
    
    def get_instuctions(self, opcode, operand):
        if(opcode == 0): 
            self.A = int(self.A/2**self.get_combo_operand(operand))
        if(opcode == 1):
            self.B ^= operand
        if(opcode == 2):
            self.B = self.get_combo_operand(operand) % 8
        if(opcode == 3):
            if(self.A != 0):
                return operand
        if(opcode == 4):
            self.B ^= self.C
        if(opcode == 5):
            return self.get_combo_operand(operand) % 8
        if(opcode == 6):
            self.B = int(self.A/2**self.get_combo_operand(operand))
        if(opcode == 7):
            self.C = int(self.A/2**self.get_combo_operand(operand))
        return -1

def compute_output(program, comp):
    output = []
    i = 0
    while i < len(program):
        if(program[i] == 5):
            output.append(comp.get_instuctions(program[i], program[i+1]))
            i += 2
        else:
            jump = comp.get_instuctions(program[i], program[i+1])
            if(jump == -1):
                i += 2
            else:
                i = jump
    return output

def question(program):
    found_all = False
    no = 0
    depts = defaultdict(list)
    depts[0] = [0]
    dept = 0
    while not found_all: # and no < 10:
        #no += 1
        start = 0
        if(dept == 0):
            start = 1
        print(depts[dept])
        if(len(depts[dept]) == 0):
            break
        for prev_A in depts[dept]:
            for j in range(start, 8):
                found_new = True
                comp = Computer(prev_A*8 + j, 0, 0)
                output = compute_output(program, comp)
                print(output, program)
                for i in range(len(output)):

                    if(output[len(output)-i-1] != program[len(program)-i-1]):
                        found_new = False
                        break
                if(found_new):
                    depts[dept+1].append(prev_A*8 + j)
                    print(depts)
                    if(len(output) == len(program)):
                        found_all = True
                        return depts
        print(depts)
        dept += 1
    return depts


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