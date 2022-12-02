"""
A = X = ROCK
B = Y = PAPER
C = Z = SCISSORS
"""


def get_score(x, y):
    match x, y:
        case "A", "X":
            return 3 + 1
        case "A", "Y":
            return 6 + 2
        case "A", "Z":
            return 0 + 3
        case "B", "X":
            return 0 + 1
        case "B", "Y":
            return 3 + 2
        case "B", "Z":
            return 6 + 3
        case "C", "X":
            return 6 + 1
        case "C", "Y":
            return 0 + 2
        case "C", "Z":
            return 3 + 3


def part1(data):
    score = 0

    for x, y in data:
        score += get_score(x, y)

    return score


################################################################################

"""
X = LOSE
Y = DRAW
Z = WIN
"""


def decider(x, y):
    match x, y:
        case "A", "X":
            return "Z"
        case "A", "Y":
            return "X"
        case "A", "Z":
            return "Y"
        case "B", "X":
            return "X"
        case "B", "Y":
            return "Y"
        case "B", "Z":
            return "Z"
        case "C", "X":
            return "Y"
        case "C", "Y":
            return "Z"
        case "C", "Z":
            return "X"


def part2(data):
    score = 0

    for x, y in data:
        option = decider(x, y)
        score += get_score(x, option)

    return score


data = open("src/day02/input.txt", "r").readlines()
# data = open("src/day02/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]
data = [line.split(" ") for line in data]


print(part1(data))
print(part2(data))
