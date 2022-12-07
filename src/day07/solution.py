import re
from pathlib import Path

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

    working_path = []

    for i, line in enumerate(data):
        line_dir = re.findall(r"^\$ cd ([^.]*)", line)

        if "cd .." in line:
            working_path.pop()
        elif line_dir:
            working_path.append(line_dir[0])
            for j, line in enumerate(data[i + 1 :]):
                if "cd " in line or i + j + 2 == len(data):
                    dirs["".join(working_path)] = calc_dir(data[i : i + j + 2])
                    break

    return dirs


def dir_fullsize(dirs):
    recursive_dir_sizes = {}

    for key in dirs.keys():
        recursive_dir_sizes[key] = dirs[key]

    for key in dirs.keys():
        subdirs = [x for x in dirs.keys() if x.startswith(key) and x is not key]
        for dir in subdirs:
            recursive_dir_sizes[key] += dirs[dir]

    return recursive_dir_sizes


def dir_tree(data):
    paths = []
    working_path = []

    for line in data:
        line_dir = re.findall(r"^\$ cd ([^.]*)", line)

        if "cd .." in line:
            working_path.pop()
        elif line_dir:
            working_path.append(line_dir[0])
            paths.append([x for x in working_path])

    return paths


def part1(data):
    dirs = dir_sizes(data)
    paths = dir_tree(data)
    recursive_sizes = dir_fullsize(dirs)

    result = 0

    for k, v in recursive_sizes.items():
        if v <= 100_000:
            result += recursive_sizes[k]

    return result


################################################################################


def part2(data):
    disk_size = 70000000
    free_space_required = 30000000

    dirs = dir_sizes(data)
    recursive_sizes = dir_fullsize(dirs)

    disk_usage = sum(dirs.values())
    unused = disk_size - disk_usage
    to_delete = free_space_required - unused

    eligable_deletions = {v for v in recursive_sizes.values() if v >= to_delete}

    result = min(eligable_deletions)

    return result


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


def auto_submitter():
    example_part1 = 95437
    example_part2 = 24933642

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
