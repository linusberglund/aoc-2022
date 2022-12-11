from pathlib import Path
from pprint import pp

from aocd import submit

################################################################################


def debug(history):
    min_x = 0
    max_x = 0

    min_y = 0
    max_y = 0

    for x, y in history:
        if min_x > x:
            min_x = x
        if x > max_x:
            max_x = x

        if min_y > y:
            min_y = y
        if y > max_y:
            max_y = y

    x_offset = 0 - min_x
    y_offset = 0 - min_y

    x_range = range(0, x_offset + max_x + 2)
    y_range = range(0, y_offset + max_y + 1)

    test = []

    for y in y_range:
        line = ""
        for x in x_range:
            if (x - x_offset, y - y_offset) in history:
                line += "#"
            else:
                line += "."

        test.append(line)

    test = test[::-1]
    for line in test:
        print("".join(line))


def step(next_dir, head_x, head_y, tail_x, tail_y):
    x = head_x
    y = head_y

    match next_dir:
        case "R":
            head_x += 1
        case "L":
            head_x -= 1
        case "U":
            head_y += 1
        case "D":
            head_y -= 1

    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        tail_x = x
        tail_y = y

    return head_x, head_y, tail_x, tail_y


def part1(data):
    head_x = 0
    head_y = 0

    tail_x = 0
    tail_y = 0

    tail_history = []

    for next_dir, y in data:
        for _ in range(y):
            head_x, head_y, tail_x, tail_y = step(
                next_dir,
                head_x,
                head_y,
                tail_x,
                tail_y,
            )
            tail_history.append((tail_x, tail_y))

    tail_history = set(tail_history)
    return len(tail_history)


################################################################################


def step_dynamic_size(next_dir, head_x, head_y, tail_x, tail_y, size):
    x = head_x
    y = head_y

    match next_dir:
        case "R":
            head_x += 1
        case "L":
            head_x -= 1
        case "U":
            head_y += 1
        case "D":
            head_y -= 1

    if abs(head_x - tail_x) > size or abs(head_y - tail_y) > size:
        tail_x = x
        tail_y = y

    return head_x, head_y, tail_x, tail_y


def part2(data):
    head_x = 0
    head_y = 0

    tail_x = 0
    tail_y = 0

    rope_length = 10

    head_history = []
    tail_history = []

    for next_dir, y in data:
        for _ in range(y):
            head_x, head_y, tail_x, tail_y = step_dynamic_size(
                next_dir,
                head_x,
                head_y,
                tail_x,
                tail_y,
                rope_length,
            )
            head_history.append((head_x, head_y))
            tail_history.append((tail_x, tail_y))

    head_history = set(head_history)
    tail_history = set(tail_history)

    debug(head_history)
    # debug(tail_history)

    print(f"Total: {len(tail_history)}, Expected: {36}")

    return len(tail_history)


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    data = [line.split(" ") for line in data]
    data = [(x, int(y)) for x, y in data]
    return data


def auto_submitter():
    example_part1 = 13
    example_part2 = 36

    if example_part1 == part1(parse("src/day09/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day09/input.txt")), part="a", day=9, year=2022)

    if example_part2 == part2(parse("src/day09/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day09/input.txt")), part="b", day=9, year=2022)


data = "src/day09/input.txt"
data = "src/day09/example.txt"
data = "src/day09/example2.txt"

print(part1(parse(data)))
print(part2(parse(data)))

# auto_submitter()
