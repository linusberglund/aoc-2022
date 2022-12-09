# isort --profile black . && black .
# python .\src\day09\solution.py
# watchexec -- "cls && python .\src\day09\solution.py"

from pathlib import Path
from pprint import pp

from aocd import submit

################################################################################

# def debug(data):
#     pass

# def get_dimensions(pos_list):
#     min_x = 0
#     max_x = 0
#     min_y = 0
#     max_y = 0

#     for pos in pos_list:
#         print(pos)
#         if pos[0] >= max_x:
#             max_x = pos[0]
#         if pos[0] <= min_x:
#             min_x = pos[0]
#         if pos[1] >= max_y:
#             max_y = pos[1]
#         if pos[1] <= min_y:
#             min_y = pos[1]

#     print(min_x, max_x, min_y, max_y)

#     return (min_x, max_x, min_y, max_y)

# def get_position_history(data):
#     pos_list = []
#     pos_list.append([0,0])

#     for x, y in data:
#         pos = [pos_list[-1][0], pos_list[-1][1]]
#         match x, y:
#             case "R", y:
#                 pos[0] += y
#             case "L", y:
#                 pos[0] -= y
#             case "U", y:
#                 pos[1] += y
#             case "D", y:
#                 pos[1] -= y
#         pos_list.append(pos)

#     return pos_list

# def create_board(dimensions):
#     min_x, max_x, min_y, max_y = dimensions

#     # []
#     # data = [[int(n) for n in line] for line in data]
#     test = [["." for x in range(min_x, max_x+1)] for y in range(min_y, max_y+1)]
#     pp(test)

#     # for x in range(min_x, max_x+1):
#     #     for y in range(min_y, max_y+1):


#     pass

# def part1(data):
#     pp(data)
#     l = get_position_history(data)
#     dim = get_dimensions(l)
#     create_board(dim)

#     return None

def step(prev_dir, next_dir, tail_x, tail_y):
    match prev_dir, next_dir:
        case "", "R":
            tail_x += 1
        case "", "L":
            tail_x -= 1
        case "", "U":
            tail_y += 1
        case "", "D":
            tail_y -= 1

        case "R", "R":
            tail_x += 1
        case "R", "L":
            pass
        case "R", "U":
            tail_x += 1
            tail_y += 1
        case "R", "D":
            tail_x += 1
            tail_y -= 1

        case "L", "R":
            pass
        case "L", "L":
            tail_x -= 1
        case "L", "U":
            tail_x -= 1
            tail_y += 1
        case "L", "D":
            tail_x -= 1
            tail_y -= 1

        case "U", "R":
            tail_x += 1
            tail_y += 1
        case "U", "L":
            tail_x -= 1
            tail_y += 1
        case "U", "U":
            tail_y += 1
        case "U", "D":
            pass

        case "D", "R":
            tail_x += 1
            tail_y -= 1
        case "D", "L":
            tail_x -= 1
            tail_y -= 1
        case "D", "U":
            pass
        case "D", "D":
            tail_y -= 1

    return tail_x, tail_y

def part1(data):
    data = data[:5]
    # pp(data)

    tail_x = 0
    tail_y = 0
    prev_dir = ""

    tail_history = []

    for next_dir, y in data:
        print(prev_dir, next_dir, y)
        for _ in range(y-1):
            tail_x, tail_y = step(prev_dir, next_dir, tail_x, tail_y)
            tail_history.append((tail_x, tail_y))
            prev_dir = next_dir
        print(tail_history)

    # print(tail_history)


    test = [["." for x in range(6)] for y in range(5)]
    count = 0
    for x,y in tail_history:
        # test[x][y] = "#"
        test[y][x] = "#"
        count += 1
    # for x in len(test):
    #     for y in len(test[0]):

    pp(test[::-1])

    result = set(tail_history)
    print(count, len(tail_history))
    print(count, len(result))

    return len(result)


################################################################################


def part2(data):
    return None


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    data = [line.split(" ") for line in data]
    data = [(x, int(y)) for x, y in data]
    return data


def auto_submitter():
    example_part1 = 13
    example_part2 = False

    if example_part1 == part1(parse("src/day09/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day09/input.txt")), part="a", day=9, year=2022)

    if example_part2 == part2(parse("src/day09/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day09/input.txt")), part="b", day=9, year=2022)


data = "src/day09/input.txt"
data = "src/day09/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

# auto_submitter()
