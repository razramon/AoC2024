from pathlib import Path
import time
from collections import defaultdict, deque

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def change_all_oc(prev, curr, gates):
    changed_gates = {}
    for gate in gates:
        g1, op, g2 = gate
        if g1 == prev:
            g1 = curr
        if g2 == prev:
            g2 = curr
        if gates[gate] == prev:
            gates[gate] = curr
        changed_gates[(g1, op, g2)] = gates[gate]
    return changed_gates


def question(gates, out_gates):
    new_gates = {}
    for gate in out_gates:
        g1, op, g2 = gate
        if (
            g1[1:] == g2[1:]
            and (g1[0] == "x" or g1[0] == "y")
            and (g2[0] == "x" or g2[0] == "y")
        ):
            if op == "XOR":
                new_gates[out_gates[gate]] = f"XOR{g1[1:]}"
            elif op == "AND":
                if g1[1:] == "00":
                    new_gates[out_gates[gate]] = f"CARRY{g1[1:]}"
                else:
                    new_gates[out_gates[gate]] = f"AND{g1[1:]}"
    changed_gates = {}
    for gate in out_gates:
        g1, op, g2 = gate
        if g1 in new_gates.keys():
            g1 = new_gates[g1]
        if g2 in new_gates.keys():
            g2 = new_gates[g2]
        if out_gates[gate] in new_gates.keys():
            out = new_gates[out_gates[gate]]
        else:
            out = out_gates[gate]
        changed_gates[(g1, op, g2)] = out
        # print("before", gate, out_gates[gate],"|", "after", (g1,op,g2), out)
    out_gates = changed_gates

    for i in range(1, 45):
        new_gates = {}
        if i < 10:
            prev = "0" + str(i - 1)
            curr = "0" + str(i)
        elif i == 10:
            curr = "10"
            prev = "09"
        else:
            curr = str(i)
            prev = str(i - 1)
        for gate in out_gates:
            g1, op, g2 = gate
            if (
                ("XOR" in g1 + g2 and "CARRY" in g1 + g2 and "_" not in g1 + g2)
                and op == "AND"
                and (
                    (g1[-2:] == curr and g2[-2:] == prev)
                    or (g1[-2:] == prev and g2[-2:] == curr)
                )
            ):
                out_gates = change_all_oc(out_gates[gate], f"CARRY_I{curr}", out_gates)

        for gate in out_gates:
            g1, op, g2 = gate
            if (
                op == "OR"
                and ("AND" in g1 + g2 and "CARRY_I" in g1 + g2)
                and g1[-2:] == g2[-2:] == curr
            ):
                out_gates = change_all_oc(out_gates[gate], f"CARRY{curr}", out_gates)
    for i in range(10):
        print(i)
        for gate in out_gates:
            g1, op, g2 = gate
            curr = f"0{i}"
            if curr in g1 or curr in g2 or curr in out_gates[gate]:
                print(gate, "->", out_gates[gate])
        print()
    for i in range(10, 46):
        print(i)
        for gate in out_gates:
            g1, op, g2 = gate
            curr = f"{i}"
            if curr in g1 or curr in g2 or curr in out_gates[gate]:
                print(gate, "->", out_gates[gate])
    return ",".join(sorted(["z05", "jst", "gdf", "mcm", "dnt", "z15", "gwc", "z30"]))


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    gates = defaultdict(int)
    for j, line in enumerate(content):
        if len(line) == 0:
            break
        line = line.split(": ")
        gates[line[0]] = int(line[1])
    out_gates = {}
    for i in range(j + 1, len(content)):
        line = content[i].split(" -> ")
        compute = line[0].split()
        out_gates[(compute[0], compute[1], compute[2])] = line[1]

    print(question(gates, out_gates))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
