def part1(data):
    largest = 0
    currentRun = 0

    for line in data:
        if line == "":
            currentRun = 0
            continue
        currentRun += int(line)
        if largest <= currentRun:
            largest = currentRun

    return largest


################################################################################


def part2(data):
    groups = []
    currentRun = 0

    for line in data:
        if line == "":
            groups.append(currentRun)
            currentRun = 0
            continue

        currentRun += int(line)

    groups = sorted(groups)

    result = groups[-1] + groups[-2] + groups[-3]

    return result


data = open("src/day01/input.txt", "r").readlines()
# data = open("src/day01/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]

print(part1(data))
print(part2(data))
