from pathlib import Path

from aocd import submit

################################################################################


def check_direction(tree, blockers):
    for x in blockers:
        if x >= tree:
            return False
    return True


def is_visible(tree, left, right, above, below):

    if check_direction(tree, left):
        return True
    if check_direction(tree, right):
        return True
    if check_direction(tree, above):
        return True
    if check_direction(tree, below):
        return True

    return False


def calc_visibility(data):
    visibility = [[None for n in line] for line in data]

    for i in range(len(data)):
        for j in range(len(data[0])):
            if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[0]) - 1:
                visibility[i][j] = True
                continue

            horizontal = data[i]
            vertical = []
            for e in range(len(data)):
                vertical.append(data[e][j])

            left = horizontal[:j]
            right = horizontal[j + 1 :]
            above = vertical[:i]
            below = vertical[i + 1 :]

            visibility[i][j] = is_visible(data[i][j], left, right, above, below)

    return visibility


def part1(data):
    visibility = calc_visibility(data)

    result = 0

    for i in range(len(visibility)):
        for j in range(len(visibility[0])):
            if visibility[i][j]:
                result += 1

    return result


################################################################################


def view_distance(tree, blockers):
    running_score = 0

    for x in blockers:
        if x >= tree:
            running_score += 1
            break

        running_score += 1

    return running_score


def scenic_score(tree, left, right, above, below):
    score_left = view_distance(tree, left)
    score_right = view_distance(tree, right)
    score_above = view_distance(tree, above)
    score_below = view_distance(tree, below)

    return score_left * score_right * score_above * score_below


def calc_scenic(data):
    scenic_map = [[0 for n in line] for line in data]

    for i in range(len(data)):
        for j in range(len(data[0])):
            if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[0]) - 1:
                continue

            horizontal = data[i]
            vertical = []
            for e in range(len(data)):
                vertical.append(data[e][j])

            left = horizontal[:j]
            right = horizontal[j + 1 :]
            above = vertical[:i]
            below = vertical[i + 1 :]

            left_from_spot = left[::-1]
            above_from_spot = above[::-1]

            scenic_map[i][j] = scenic_score(
                data[i][j], left_from_spot, right, above_from_spot, below
            )

    return scenic_map


def part2(data):
    scenic_overview = calc_scenic(data)

    max_score = 0

    for i in range(len(scenic_overview)):
        for j in range(len(scenic_overview[0])):
            if scenic_overview[i][j] > max_score:
                max_score = scenic_overview[i][j]

    return max_score


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    data = [[int(n) for n in line] for line in data]
    return data


def auto_submitter():
    example_part1 = 21
    example_part2 = 8

    if example_part1 == part1(parse("src/day08/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day08/input.txt")), part="a", day=8, year=2022)

    if example_part2 == part2(parse("src/day08/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day08/input.txt")), part="b", day=8, year=2022)


data = "src/day08/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

auto_submitter()
