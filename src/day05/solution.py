import re
from pathlib import Path

from aocd import submit

################################################################################


def step(crates, source, target):

    if len(crates[source]) == 0:
        return crates

    grabbed = crates[source].pop()
    crates[target].append(grabbed)
    return crates


def run_operation(crates, procedure):
    amount, source, target = procedure

    for _ in range(amount):
        crates = step(crates, source, target)

    return crates


def get_topmost(crates, stacks):
    topmost = []

    for i in range(stacks):
        i += 1

        if len(crates[i]) == 0:
            continue

        topmost.append(crates[i][-1])

    result = "".join(topmost)

    return result


def part1(data):
    stacks, crates, procedures = data

    for procedure in procedures:
        run_operation(crates, procedure)

    result = get_topmost(crates, stacks)

    return result


################################################################################


def run_operation_CrateMover_9001(crates, procedure):
    amount, source, target = procedure

    grabbed = []

    for _ in range(amount):
        grabbed.append(crates[source].pop())

    grabbed = grabbed[::-1]
    crates[target].extend(grabbed)
    return crates


def part2(data):
    stacks, crates, procedures = data

    for procedure in procedures:
        run_operation_CrateMover_9001(crates, procedure)

    result = get_topmost(crates, stacks)

    return result


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()

    stacks = 0
    crates = {}
    procedures = []

    stack_line = 0

    for line_index, line in enumerate(data):
        if re.match(r"^\s*\d", line):
            stack_line = line_index
            stacks = int(re.findall(r"(\d+)\s*$", line)[0])

    for line_index, line in enumerate(data):
        if line_index >= stack_line:
            break

        line = re.sub(r"(?:\[| )( |[A-Z])(?:\]| )(?: |$)", r"\g<1>", line)
        # line = line.replace("   ", " ")

        for char_index, char in enumerate(line):
            char_index += 1

            if char != "0":
                current_stack = crates.get(char_index, [])
                current_stack.append(char)
                crates[char_index] = current_stack

    procedure_data = data[stack_line + 2 :]
    for line in procedure_data:
        test = re.findall(r"move (\d+) from (\d+) to (\d+)", line)[0]
        test = [int(x) for x in test]
        procedures.append(tuple(test))

    for key in crates.keys():
        new = crates[key][::-1]
        new = [x for x in new if x != " "]
        crates[key] = new

    return stacks, crates, procedures


def auto_submitter():
    example_part1 = "CMZ"
    example_part2 = "MCD"

    if example_part1 == part1(parse("src/day05/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day05/input.txt")), part="a", day=5, year=2022)

    if example_part2 == part2(parse("src/day05/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day05/input.txt")), part="b", day=5, year=2022)


data = "src/day05/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

auto_submitter()
