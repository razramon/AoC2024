from pathlib import Path
import time
from collections import deque
SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")



def question(machines):
    ans = 0
    for machine in machines:
        a = machine[0]
        b = machine[1]
        x = machine[2]
        i = (x[0]*b[1] - b[0]*x[1])/(a[0]*b[1] - a[1]*b[0])
        j = (x[1] - a[1]*i)/b[1]
        if(i.is_integer() and j.is_integer()):
            ans += int(j) + int(i)*3
    return ans


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    machines = []
    for i in range(0, len(content), 4):
        machine = []
        for j in range(i, i + 3):
            line = content[j].split(":")[1].split(",")
            if "+" in line[0]:
                x = int(line[0].split("+")[1])
                y = int(line[1].split("+")[1])
            else:
                x = int(line[0].split("=")[1]) + 10000000000000
                y = int(line[1].split("=")[1]) + 10000000000000
            machine.append([x, y])
        machines.append(machine)

    print(question(machines))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
