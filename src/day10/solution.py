from pathlib import Path

from aocd import submit

################################################################################


def part1(data):
    x = 1
    v = 0
    cycle = 0
    execution = 0

    history = {}

    for line in data:
        if "noop" in line:
            execution += 1
        elif "addx" in line:
            execution += 2
            v = int(line[1])

        while execution > 0:
            cycle += 1
            execution -= 1

            history[cycle] = x

            if execution == 0 and v != 0:
                x += v
                v = 0

    result = 0

    for k, v in history.items():
        if k in [20, 60, 100, 140, 180, 220]:
            result += k * v

    return result


################################################################################


def debug(crt):
    for line in crt:
        l = "".join(line)
        print(l)


def part2(data):
    x = 1
    v = 0
    cycle = 0
    execution = 0

    crt = [[" " for x in range(40)] for y in range(6)]

    for line in data:
        if "noop" in line:
            execution += 1
        elif "addx" in line:
            execution += 2
            v = int(line[1])

        while execution > 0:
            a, b = divmod(cycle, 40)

            if x == b or x - 1 == b or x + 1 == b:
                crt[a][b] = "#"

            cycle += 1
            execution -= 1

            if execution == 0 and v != 0:
                x += v
                v = 0

    return debug(crt)


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    data = [line.split(" ") for line in data]
    return data


def auto_submitter():
    example_part1 = 13140
    example_part2 = False

    if example_part1 == part1(parse("src/day10/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day10/input.txt")), part="a", day=10, year=2022)

    if example_part2 == part2(parse("src/day10/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day10/input.txt")), part="b", day=10, year=2022)


data = "src/day10/input.txt"
# data = "src/day10/example.txt"
# data = "src/day10/example2.txt"

print(part1(parse(data)))
print(part2(parse(data)))

auto_submitter()
