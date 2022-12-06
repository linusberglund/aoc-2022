from pathlib import Path

from aocd import submit

################################################################################


def part1(data):
    for i, char in enumerate(data):

        if i < 3:
            continue

        sliding_window = set()
        sliding_window.add(data[i])
        sliding_window.add(data[i - 1])
        sliding_window.add(data[i - 2])
        sliding_window.add(data[i - 3])

        if len(sliding_window) == 4:
            return i + 1

    return None


################################################################################


def part2(data):
    for i, char in enumerate(data):

        if i < 14:
            continue

        sliding_window = set()
        for j in range(0, 14):
            sliding_window.add(data[i - j])

        if len(sliding_window) == 14:
            return i + 1

    return None


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()[0]
    return data


def auto_submitter():
    example_part1 = 7
    example_part2 = 19

    if example_part1 == part1(parse("src/day06/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day06/input.txt")), part="a", day=6, year=2022)

    if example_part2 == part2(parse("src/day06/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day06/input.txt")), part="b", day=6, year=2022)


data = "src/day06/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

auto_submitter()
