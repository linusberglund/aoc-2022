import re


def get_common(backpack):
    line_length = int(len(backpack) / 2)
    left = backpack[:line_length]
    right = backpack[line_length:]

    common = set()

    for i in left:
        for j in right:
            if i == j:
                common.add(i)

    return common


def get_prio(backpack):
    prio = 0

    for char in backpack:
        if re.match("[A-Z]", char):
            prio += ord(char) - 38
        if re.match("[a-z]", char):
            prio += ord(char) - 96

    return prio


def part1(data):
    total_prio = 0
    for line in data:
        common = get_common(line)
        total_prio += get_prio(common)

    return total_prio


################################################################################


def get_badge(backpacks):
    badge = set()

    for x in backpacks[0]:
        for y in backpacks[1]:
            for z in backpacks[2]:
                if x == y == z:
                    badge.add(x)

    return badge


def part2(data):
    total_prio = 0
    for i in range(0, len(data), 3):
        badge = get_badge(data[i : i + 3])
        total_prio += get_prio(badge)
    return total_prio


data = open("src/day03/input.txt", "r").readlines()
# data = open("src/day03/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]

print(part1(data))
print(part2(data))

data = open("src/day03/example.txt", "r").readlines()
data = [line.strip("\n") for line in data]
print("PART 1 EXAMPLE PASS") if part1(data) == 157 else None
print("PART 2 EXAMPLE PASS") if part2(data) == 70 else None
