# isort --profile black . && black .
# python .\src\day14\solution.py
# watchexec -- "cls && python .\src\day14\solution.py"

from pathlib import Path
from pprint import pp

from aocd import submit

################################################################################


def add_rock_line(rock_chart: set, rock_line):
    start, end = rock_line

    x0, y0 = start
    x1, y1 = end

    if x0 < x1:
        x_range = range(x0, x1 + 1)
    else:
        x_range = range(x1, x0 + 1)

    if y0 < y1:
        y_range = range(y0, y1 + 1)
    else:
        y_range = range(y1, y0 + 1)

    for x in x_range:
        rock_chart.add((x, y1))

    for y in y_range:
        rock_chart.add((x0, y))


def add_rock_path(rock_chart, rock_path):
    for i in range(len(rock_path) - 1):
        rock_line = (rock_path[i], rock_path[i + 1])
        add_rock_line(rock_chart, rock_line)


def part1(data):
    rock_chart = set()

    for rock_path in data:
        add_rock_path(rock_chart, rock_path)

    # 496,6, 497,6, 498,4, 498,5, 498,6
    pp(sorted(rock_chart))

    return None


################################################################################


def part2(data):
    return None


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    data = [x.split(" -> ") for x in data]
    data = [[x.split(",") for x in line] for line in data]
    data = [[[int(x) for x in y] for y in line] for line in data]
    return data


def auto_submitter():
    example_part1 = 24
    example_part2 = False

    if example_part1 == part1(parse("src/day14/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day14/input.txt")), part="a", day=14, year=2022)

        if example_part2 == part2(parse("src/day14/example.txt")):
            print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
            submit(part2(parse("src/day14/input.txt")), part="b", day=14, year=2022)


data = "src/day14/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

# auto_submitter()
