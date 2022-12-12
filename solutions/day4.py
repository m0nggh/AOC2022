def parse_input():
    data = []
    file = open("inputs/day4.txt", "r")
    line = file.readline().strip()
    while line != '':
        data.append(line)
        line = file.readline().strip()
    # final data format: ['2-4,6-8', '2-3,4-5']
    return data


def part_one(data):
    # calculate number of overlapping pairs where one range fully covers the other
    total = 0
    for row in data:
        first, second = row.split(",")
        first_start, first_end = first.split("-")
        first_start, first_end = int(first_start), int(first_end)
        second_start, second_end = second.split("-")
        second_start, second_end = int(second_start), int(second_end)
        # 2 scenarios for full overlap
        if first_start <= second_start and first_end >= second_end or second_start <= first_start and second_end >= first_end:
            total += 1
    return total


def part_two(data):
    # calculate number of overlapping pairs where one range partially covers the other
    # method: find non overlaps and then subtract from total
    total = no_overlap = 0
    for row in data:
        first, second = row.split(",")
        first_start, first_end = first.split("-")
        first_start, first_end = int(first_start), int(first_end)
        second_start, second_end = second.split("-")
        second_start, second_end = int(second_start), int(second_end)
        # 2 scenarios for no overlap
        if first_end < second_start or first_start > second_end:
            no_overlap += 1
        total += 1
    return total - no_overlap


if __name__ == "__main__":
    data = parse_input()
    # print(data)
    print(part_one(data))
    print(part_two(data))
