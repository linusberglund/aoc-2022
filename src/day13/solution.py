# isort --profile black . && black .
# python .\src\day13\solution.py
# watchexec -- "cls && python .\src\day13\solution.py"

from pathlib import Path
from pprint import pp

from aocd import submit

################################################################################


def pad_list(left, right):
    if len(left) > len(right):
        for _ in range(len(left) - len(right)):
            right.append(None)
    if len(right) > len(left):
        for _ in range(len(right) - len(left)):
            left.append(None)

    return left, right


def compare(p1, p2):
    print(p1)
    print(p2)
    p1, p2 = pad_list(p1, p2)
    print(p1)
    print(p2)

    for left, right in zip(p1, p2):
        if type(left) is type(0) and type(right) is type(0):
            if left < right:
                return True
            if left > right:
                return False
            if left == right:
                continue

        if type(left) is type([]) and type(right) is type([]):
            print("ALREADY")
            left, right = pad_list(left, right)
            for x, y in zip(left, right):
                pass

        if type(left) is type(0):
            left = [left]

        if type(right) is type(0):
            right = [right]

        return compare(left, right)

    return False


def part1(data):
    # a = [0]
    # b = [1, 2]
    # a, b = pad_list(a, b)
    # for x in zip(a, b, strict=True):
    #     print(x)

    result = 0
    pairs = []

    for i in range(0, len(data), 3):
        pairs.append((eval(data[i]), eval(data[i + 1])))

    for i, (left, right) in enumerate(pairs):
        if compare(left, right):
            result += i + 1
        print("RES:", result)

    print()
    return result


################################################################################


def part2(data):
    return None


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


def auto_submitter():
    example_part1 = 13
    example_part2 = False

    if example_part1 == part1(parse("src/day13/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day13/input.txt")), part="a", day=13, year=2022)

    if example_part2 == part2(parse("src/day13/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day13/input.txt")), part="b", day=13, year=2022)


data = "src/day13/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

# auto_submitter()
