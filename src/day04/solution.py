from pathlib import Path

from aocd import submit


def get_overlap(pair):
    x0, y0 = pair[0].split("-")
    x1, y1 = pair[1].split("-")
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)

    overlap_range = max(x0, x1), min(y0 - 1, y1 - 1) + 1
    return overlap_range


def is_contained(pair, overlap):
    x0, y0 = pair[0].split("-")
    x1, y1 = pair[1].split("-")
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)

    if overlap[0] <= x0 and overlap[1] >= y0:
        return pair

    if overlap[0] <= x1 and overlap[1] >= y1:
        return pair

    return None


def part1(data):
    pairs = []

    for line in data:
        overlap = get_overlap(line)
        contained = is_contained(line, overlap)

        if contained != None:
            pairs.append(line)

    return len(pairs)


################################################################################


def is_contained_at_all(pair, overlap):
    x0, y0 = pair[0].split("-")
    x1, y1 = pair[1].split("-")
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)

    if overlap[0] <= overlap[1]:
        return pair

    return None


def part2(data):
    pairs = []

    for line in data:
        overlap = get_overlap(line)
        contained = is_contained_at_all(line, overlap)

        if contained != None:
            pairs.append(line)

    return len(pairs)


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    data = [line.split(",") for line in data]
    return data


def auto_submitter():
    example_part1 = 2
    example_part2 = 4

    if example_part1 == part1(parse("src/day04/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day04/input.txt")), part="a", day=4, year=2022)

    if example_part2 == part2(parse("src/day04/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day04/input.txt")), part="b", day=4, year=2022)


data = parse("src/day04/example.txt")

print(part1(data))
print(part2(data))

auto_submitter()
