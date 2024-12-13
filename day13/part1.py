from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def search_match(machine):
    x = [[machine[0][0] * i, machine[0][1] * i] for i in range(101)]
    y = [[machine[1][0] * i, machine[1][1] * i] for i in range(101)]

    for i, a in enumerate(x):
        for j, b in enumerate(y):
            if a[0] + b[0] == machine[2][0] and a[1] + b[1] == machine[2][1]:
                return i * 3 + j
    return 0


def question(machines):
    ans = 0
    for machine in machines:
        ans += search_match(machine)

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
                x = int(line[0].split("=")[1])
                y = int(line[1].split("=")[1])
            machine.append([x, y])
        machines.append(machine)

    print(question(machines))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
