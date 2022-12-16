from pathlib import Path

from aocd import submit

################################################################################


def pad_list(left, right):
    if len(left) > len(right):
        for _ in range(len(left) - len(right)):
            right.append(None)
    if len(right) > len(left):
        for _ in range(len(right) - len(left)):
            left.append(None)

    return left, right


def compare(p1, p2):
    if p1 is None:
        return True
    if p2 is None:
        return False

    if type(p1) is type(0) and type(p2) is type(0) and p1 == p2:
        return None
    if type(p1) is type(0) and type(p2) is type(0) and p1 < p2:
        return True
    if type(p1) is type(0) and type(p2) is type(0) and p1 > p2:
        return False

    if type(p1) is not type([]):
        p1 = [p1]

    if type(p2) is not type([]):
        p2 = [p2]

    if type(p1) is type([]) and type(p2) is type([]):
        p1, p2 = pad_list(p1, p2)
    big_zip = zip(p1, p2, strict=True)

    for left, right in big_zip:

        if type(left) is type(0) and type(right) is type(0):
            if left == right:
                continue
            if left < right:
                return True
            if left > right:
                return False

        if type(left) is type([]) and type(right) is type([]):
            left, right = pad_list(left, right)
            small_zip = zip(left, right, strict=True)

            for x, y in small_zip:
                result = compare(x, y)
                if result is not None:
                    return result

        if type(left) is type(0):
            left = [left]

        if type(right) is type(0):
            right = [right]

        result = compare(left, right)
        if result is not None:
            return result

    return None


def part1(data):
    pairs = []

    for i in range(0, len(data), 3):
        pairs.append((eval(data[i]), eval(data[i + 1])))

    result = 0

    for i, (left, right) in enumerate(pairs):
        if compare(left, right):
            result += i + 1

    return result


################################################################################


def part2(data):
    packets = [x for x in data if x != ""]

    divider_packet_1 = "[[2]]"
    divider_packet_2 = "[[6]]"

    packets.append(divider_packet_1)
    packets.append(divider_packet_2)

    for i in range(1, len(packets)):
        for j in range(i - 1, -1, -1):
            if not compare(eval(packets[j]), eval(packets[j + 1])):
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

    divider_packet_1_index = packets.index(divider_packet_1) + 1
    divider_packet_2_index = packets.index(divider_packet_2) + 1

    decoder_key = divider_packet_1_index * divider_packet_2_index

    return decoder_key


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


def auto_submitter():
    example_part1 = 13
    example_part2 = 140

    if example_part1 == part1(parse("src/day13/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day13/input.txt")), part="a", day=13, year=2022)

        if example_part2 == part2(parse("src/day13/example.txt")):
            print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
            submit(part2(parse("src/day13/input.txt")), part="b", day=13, year=2022)


data = "src/day13/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

auto_submitter()
