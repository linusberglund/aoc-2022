import re
from pathlib import Path

from aocd import submit

################################################################################


def debug_monkeys(monkeys):
    for m in monkeys:
        print(m["items"])
    print("----------")


def step_turn(monkey_index, monkeys):
    m = monkeys[monkey_index]

    for _ in range(len(m["items"])):
        current_item = m["items"].pop(0)

        match m["op"][0], m["op"][1]:
            case "+", "old":
                current_item += current_item
            case "*", "old":
                current_item *= current_item
            case "+", _:
                current_item += int(m["op"][1])
            case "*", _:
                current_item *= int(m["op"][1])

        current_item = int(current_item / 3)
        m["inspections"] += 1

        if current_item % m["divisor"] == 0:
            monkeys[m["if_true"]]["items"].append(current_item)
        else:
            monkeys[m["if_false"]]["items"].append(current_item)

    return monkeys


def step_round(monkeys):
    for i in range(len(monkeys)):
        monkeys = step_turn(i, monkeys)

    return monkeys


def part1(data):

    rounds = 20

    for _ in range(rounds):
        data = step_round(data)
        pass

    activity = []

    for x in data:
        activity.append(x["inspections"])

    activity = sorted(activity)[::-1]
    monkey_business = activity[0] * activity[1]

    return monkey_business


################################################################################


def step_turn_2(monkey_index, monkeys, common_multiple):
    m = monkeys[monkey_index]

    for _ in range(len(m["items"])):
        current_item = m["items"].pop(0)

        match m["op"][0], m["op"][1]:
            case "+", "old":
                current_item += current_item
            case "*", "old":
                current_item *= current_item
            case "+", _:
                current_item += int(m["op"][1])
            case "*", _:
                current_item *= int(m["op"][1])

        m["inspections"] += 1

        if current_item % m["divisor"] == 0:
            monkeys[m["if_true"]]["items"].append(current_item % common_multiple)
        else:
            monkeys[m["if_false"]]["items"].append(current_item % common_multiple)

    return monkeys


def step_round_2(monkeys, common_multiple):
    for i in range(len(monkeys)):
        monkeys = step_turn_2(i, monkeys, common_multiple)

    return monkeys


def part2(data):

    rounds = 10_000

    common_multiple = 1
    for x in data:
        common_multiple *= x["divisor"]
    print(common_multiple)

    for _ in range(rounds):
        data = step_round_2(data, common_multiple)

    activity = []
    [activity.append(x["inspections"]) for x in data]
    activity = sorted(activity)[::-1]
    monkey_business = activity[0] * activity[1]
    return monkey_business


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()

    monkeys = []

    for i, line in enumerate(data):
        if "Monkey" in line:

            items = re.findall(r"items: (.*)", data[i + 1])[0].replace(" ", "")
            items = [int(n) for n in items.split(",")]

            op = re.findall(r"Operation: new = old (.*)", data[i + 2])[0].split(" ")
            divisor = int(re.findall(r"Test: divisible by (\d+)", data[i + 3])[0])
            if_true = int(re.findall(r"true: throw to monkey (\d+)", data[i + 4])[0])
            if_false = int(re.findall(r"false: throw to monkey (\d+)", data[i + 5])[0])

            monkeys.append(
                {
                    "items": items,
                    "op": op,
                    "divisor": divisor,
                    "if_true": if_true,
                    "if_false": if_false,
                    "inspections": 0,
                }
            )

    return monkeys


def auto_submitter():
    example_part1 = 10605
    example_part2 = 2713310158

    if example_part1 == part1(parse("src/day11/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day11/input.txt")), part="a", day=11, year=2022)

    if example_part2 == part2(parse("src/day11/example.txt")):
        print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
        submit(part2(parse("src/day11/input.txt")), part="b", day=11, year=2022)


data = "src/day11/input.txt"
data = "src/day11/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

auto_submitter()
