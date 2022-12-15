# isort --profile black . && black .
# python .\src\day15\solution.py
# watchexec -- "cls && python .\src\day15\solution.py"

import re
from pathlib import Path
from pprint import pp

from aocd import submit

################################################################################


def debug(chart: dict, dimensions):

    min_x, max_x, min_y, max_y = dimensions

    x_range = range(min_x, max_x + 1)
    y_range = range(min_y, max_y + 1)

    test = []

    for y in y_range:

        # if y_index < 10:
        #     y_index = f" {y_index}"
        # line = f"{y_index} "
        line = ""

        for x in x_range:
            if (x, y) in chart.keys():
                line += chart[(x, y)]
            else:
                line += "."

        test.append(line)

    for line in test:
        print("".join(line))


def add_sensors_beacons(chart, data):
    for line in data:
        sx, sy, bx, by = line
        chart[(sx, sy)] = "S"
        chart[(bx, by)] = "B"


# -1,0, 1,0, 0,-1, 0,1

# .....
# ..#..
# .#S#.
# ..#..
# .....

# -2,0, 2,0, 0,-2, 0,2 | 1,1, -1,-1, 1,-1, -1,1

# ..#..
# .###.
# ##S##
# .###.
# ..#..


def scan(chart, data):
    for line in data:
        print(f"PROCESSING: {line}")
        sx, sy, bx, by = line

        # TEST
        # Sensor at x=8, y=7: closest beacon is at x=2, y=10
        # sx, sy, bx, by = (8, 7, 2, 10)

        # TEST 2
        # Sensor at x=2, y=0: closest beacon is at x=2, y=10
        # sx, sy, bx, by = (2, 0, 2, 10)

        manhattan_distance = abs(bx - sx) + abs(by - sy)
        print(manhattan_distance)

        for i in range(-manhattan_distance, manhattan_distance + 1):

            debug(chart, get_chart_dimensions(chart))
            print()

            for j in range(-i, i + 1):

                above = (sx - j, sy + i - manhattan_distance)

                if above not in chart or chart[(above)] not in ["S", "B"]:
                    chart[above] = "#"

                below = (sx - j, sy - i + manhattan_distance)

                if below not in chart or chart[(below)] not in ["S", "B"]:
                    chart[below] = "#"


# def get_initial_dimensions(data):

#     min_x = 0
#     max_x = 0

#     min_y = 0
#     max_y = 0

#     for line in data:
#         sx, sy, bx, by = line
#         min_x = min(min_x, sx, bx)
#         max_x = max(max_x, sx, bx)
#         min_y = min(min_y, sy, by)
#         max_y = max(max_y, sy, by)

#     return (min_x, max_x, min_y, max_y)


def get_chart_dimensions(chart):
    min_x = 0
    max_x = 0

    min_y = 0
    max_y = 0

    for x, y in chart.keys():
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    return (min_x, max_x, min_y, max_y)


def part1(data):

    chart = {}
    add_sensors_beacons(chart, data)
    scan(chart, data)

    dimensions = get_chart_dimensions(chart)
    # debug(chart, dimensions)

    row_of_interest = 2000000

    row = []

    min_x, max_x, min_y, max_y = dimensions
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            if y == row_of_interest:
                if (x, y) in chart:
                    row.append(chart[(x, y)])
                else:
                    row.append(".")

    row = [x for x in row if x == "#"]

    print()
    print(f"RES: {''.join(row)}")
    print(len(row))

    return len(row)


################################################################################


def part2(data):
    return None


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    data = [
        re.findall(r"^.*?x=([^,:]+).*?y=([^,:]+).*?x=([^,:]+).*?y=([^,:]+)$", x)
        for x in data
    ]
    data = [x[0] for x in data]
    data = [[int(x) for x in line] for line in data]
    return data


def auto_submitter():
    example_part1 = 26
    example_part2 = False

    if example_part1 == part1(parse("src/day15/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day15/input.txt")), part="a", day=15, year=2022)

        if example_part2 == part2(parse("src/day15/example.txt")):
            print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
            submit(part2(parse("src/day15/input.txt")), part="b", day=15, year=2022)


data = "src/day15/example.txt"
data = "src/day15/input.txt"

print(part1(parse(data)))
# print(part2(parse(data)))

# auto_submitter()
