# isort --profile black . && black .
# python .\src\day12\solution.py
# watchexec -- "cls && python .\src\day12\solution.py"

import sys
from pathlib import Path
from pprint import pp

from aocd import submit

################################################################################


def debug(chart, visited):
    for y in chart:
        print("".join(y))

    visited_chart = [["." for n in line] for line in chart]

    for y in range(len(visited_chart)):
        for x in range(len(visited_chart[0])):
            if (x, y) in visited:
                visited_chart[y][x] = "#"

    for y in visited_chart:
        print("".join(y))

    pass


def dijkstra(graph, chart, start):
    dist = {}
    prev = {}
    Q = set()

    for v in graph:
        dist[v] = sys.maxsize
        prev[v] = None
        Q.add(v)

    dist[start] = 0

    while Q:
        min_dist = sys.maxsize
        u = None

        for v in Q:
            if dist[v] < min_dist:
                u = v

        if u is None:
            u = Q.pop()
        else:
            Q.remove(u)

        u_x, u_y = u

        neighbors = []
        neighbors.append((u_x + 1, u_y))
        neighbors.append((u_x, u_y + 1))
        neighbors.append((u_x - 1, u_y))
        neighbors.append((u_x, u_y - 1))

        neighbors = [n for n in neighbors if n in Q]

        for v in neighbors:
            alt = dist[u]

            v_x, v_y = v

            current_elevation = ord(chart[v_y][v_x])
            if chart[v_y][v_x] == "E":
                current_elevation = ord("z") + 1

            if chart[u_y][u_x] not in ["S", "E"]:
                if current_elevation > ord(chart[u_y][u_x]) + 1:
                    alt = sys.maxsize
                else:
                    alt += 1

            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


def part1(data):

    graph = set()
    start = None
    goal = None

    for y in range(len(data)):
        for x in range(len(data[0])):
            graph.add((x, y))
            if data[y][x] == "S":
                start = (x, y)
            if data[y][x] == "E":
                goal = (x, y)

    dist, prev = dijkstra(graph, data, start)

    path = []
    current = goal

    while True:
        if current == start:
            break
        path.append(current)
        current = prev[current]

    # debug(data, path)
    return len(path)


################################################################################


def part2(data):
    return None


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    data = [[n for n in line] for line in data]
    return data


def auto_submitter():
    example_part1 = 31
    example_part2 = False

    if example_part1 == part1(parse("src/day12/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day12/input.txt")), part="a", day=12, year=2022)

    if example_part2 == part2(parse("src/day12/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day12/input.txt")), part="b", day=12, year=2022)


data = "src/day12/input.txt"
data = "src/day12/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

auto_submitter()
