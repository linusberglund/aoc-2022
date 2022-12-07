# isort --profile black . && black .
# python .\src\day07\solution.py
# watchexec -- "cls && python .\src\day07\solution.py"

import os
import re
import statistics
import time
from enum import Enum
from pathlib import Path
from pprint import pp

from aocd import submit

################################################################################


def calc_dir(data):
    total = 0

    for line in data:
        n = re.findall(r"^(\d+)", line)
        if n:
            total += int(n[0])

    return total


def dir_sizes(data):
    dirs = {}

    for i, line in enumerate(data):
        if "cd .." in line:
            continue
        if "cd " in line:
            folder_name = re.findall(r"^\$ cd ([^.])", line)[0]
            for j, line in enumerate(data[i + 1 :]):
                if "cd " in line or i + j + 2 == len(data):
                    dirs[folder_name] = calc_dir(data[i : i + j + 2])
                    break

    return dirs


def dir_tree(data):
    paths = []
    working_path = []

    for line in data:
        line_dir = re.findall(r"^\$ cd ([^.])", line)

        if "cd .." in line:
            working_path.pop()
        elif line_dir:
            working_path.append(line_dir[0])
            paths.append([x for x in working_path])

    return paths


# - /
#   - a
#     - e
#   - d

# [['/'], ['/', 'a'], ['/', 'a', 'e'], ['/', 'd']]

# Solution useless, assumes unique folder/file names

def part1(data):
    dirs = dir_sizes(data)
    paths = dir_tree(data)

    print(dirs)
    print(paths)

    totals = {}

    for dir in dirs.keys():
        totals[dir] = 0


    # >:(


    # for dir in "/": #dirs.keys():
    #     full_path = []

    #     for path in paths:
    #         if path[-1] == dir:
    #             full_path = path
    #             break

    #     for current_dir in full_path:
    #         totals[dir] += dirs[current_dir]

    # print(totals)

    # for path in paths:
    #     for dir in path:
    #         totals[dir] += dirs[dir]

    # for path in paths:
    #     running_sum = 0
    #     for x in path:
    #         running_sum += dirs[x]
    #     print(running_sum)

    print(totals)

    return None


################################################################################


def part2(data):
    return None


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()

    # data = [[int(n) for n in line] for line in data]
    # data = [int(n) for n in data]
    # data = [line.split(" ") for line in data]
    # data = [line.split("-") for line in data]
    # data = [line.split(",") for line in data]
    # data = [line.split(",") for line in data][0]
    # data = [line.strip("\n") for line in data]
    # data = [line[:-1] for line in data]
    # data = [re.sub(r" -> ", r",", line) for line in data]
    # data = [re.sub(r" \| ", r" ", line) for line in data]
    # data = data[0]

    return data


def auto_submitter():
    example_part1 = 95437
    example_part2 = False

    if example_part1 == part1(parse("src/day07/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day07/input.txt")), part="a", day=7, year=2022)

    if example_part2 == part2(parse("src/day07/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day07/input.txt")), part="b", day=7, year=2022)


data = "src/day07/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

auto_submitter()
