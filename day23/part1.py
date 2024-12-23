from pathlib import Path
import time
from collections import defaultdict, deque

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def question(graph):
    ans = set()
    for x in graph:
        if x[0] == "t":
            seen = set()
            queue = deque([[[x], 0]])
            while queue:
                curr, dept = queue.popleft()
                if dept == 2:
                    if x in graph[curr[-1]]:
                        ans.add(tuple(sorted(curr)))
                if curr[-1] in seen:
                    continue
                seen.add(curr[-1])
                for neigh in graph[curr[-1]]:
                    if dept < 2 and neigh not in seen:
                        queue.append([curr + [neigh], dept + 1])
    return len(ans)


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
