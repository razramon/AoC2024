from pathlib import Path
import time
from collections import defaultdict, deque

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def get_threes(graph):
    ans = set()
    for x in graph:
        seen = set()
        queue = deque([[[x], 0]])
        while queue:
            curr, dept = queue.popleft()
            if dept == 2:
                if x in graph[curr[-1]]:
                    ans.add(tuple(sorted(curr)))
            else:
                if curr[-1] in seen:
                    continue
                seen.add(curr[-1])
                for neigh in graph[curr[-1]]:
                    if dept < 2 and neigh not in seen:
                        queue.append([curr + [neigh], dept + 1])
    return ans


def question(graph):
    threes = get_threes(graph)
    ans = []
    for t in threes:
        connected = list(t)
        queue = deque(connected)
        seen = set()
        while queue:
            curr = queue.popleft()
            if curr in seen:
                continue
            seen.add(curr)
            for neigh in graph[curr]:
                if neigh not in seen:
                    if sum([1 if x in graph[neigh] else 0 for x in connected]) == len(
                        connected
                    ):
                        connected.append(neigh)
                        queue.append(neigh)

        if len(connected) > len(ans):
            ans = connected

    return ",".join(sorted(ans))


def main():
    with open(INPUT_FILE, mode="rt") as f:
        content = f.read().splitlines()
    graph = defaultdict(list)
    for line in content:
        line = line.split("-")
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
    print(question(graph))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
