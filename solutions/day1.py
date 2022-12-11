def parse_input():
    data = []
    with open("inputs/day1.txt", "r") as file:
        data = file.read().split("\n\n")  # split by two lines
    for i in range(len(data)):
        line = data[i].strip().split("\n")  # one elf
        data[i] = list(map(int, line))
    # final data format: [[123, 456], [789]]
    return data


def part_one(data):
    # find most calories
    return max([sum(row) for row in data])


def part_two(data):
    # find sum of top 3 max calories
    sorted_sums = sorted([sum(row) for row in data], reverse=True)
    return sorted_sums[0] + sorted_sums[1] + sorted_sums[2]


if __name__ == "__main__":
    data = parse_input()
    print(part_one(data))
    print(part_two(data))
