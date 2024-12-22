from pathlib import Path
import time
SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")
from termcolor import colored
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
        if(opcode == 0): #adv
            self.A = self.A*(2**self.get_combo_operand(operand))
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
            self.B = self.A*(2**self.get_combo_operand(operand))
        if(opcode == 7):
            self.C = self.A*(2**self.get_combo_operand(operand))
        print(self.A, self.B, self.C)
        return -1

# 2,4,1,5,7,5,1,6,0,3,4,2,5,5,3,0



def question(comp, program):
    output = []
    while len(output) < len(program):
        i = len(program) - 2
        while i >= 0:
            if(program[i] == 5):
                output.append(comp.get_instuctions(program[i], program[i+1]))
            comp.get_instuctions(program[i], program[i+1])
            i -= 2
        print(output)
    print(comp.A, comp.B, comp.C)

def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    A = 0
    B = int(content[1].split()[-1])
    C = int(content[2].split()[-1])
    comp = Computer(A, B, C)
    program = [int(x) for x in content[4].split()[-1].split(",")]

    question(comp, program)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")