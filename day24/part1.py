from pathlib import Path
import time
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def compute_gate(g1, g2, op):
    if op == "AND":
        return g1 and g2
    if op == "OR":
        return g1 or g2
    if op == "XOR":
        return g1 ^ g2


def binatointeger(binary):
    number = 0
    for _, b in binary:
        number = (2 * number) + b
    return number


def question(gates, out_gates):
    ans = []
    while len(out_gates) > 0:
        to_remove = []
        for key in out_gates:
            g1, op, g2 = key
            if g1 in gates.keys() and g2 in gates.keys():
                gate = compute_gate(gates[g1], gates[g2], op)
                for k in out_gates[key]:
                    gates[k] = gate
                to_remove.append(key)
        while to_remove:
            key = to_remove.pop()
            del out_gates[key]
    for g in gates:
        if g[0] == "z":
            ans.append([g, gates[g]])
    ans.sort(key=lambda x: x[0], reverse=True)
    return binatointeger(ans)


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    gates = defaultdict(int)
    for j, line in enumerate(content):
        if len(line) == 0:
            break
        line = line.split(": ")
        gates[line[0]] = int(line[1])
    out_gates = defaultdict(list)
    for i in range(j + 1, len(content)):
        line = content[i].split(" -> ")
        compute = line[0].split()
        out_gates[(compute[0], compute[1], compute[2])].append(line[1])
    print(question(gates, out_gates))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
