def parse_input():
    data = []
    file = open("inputs/day10.txt", "r")
    line = file.readline().strip()
    while line != '':
        # store 0 if noop
        splitted = line.split()
        if len(splitted) == 1:
            data.append(0)
        else:
            # store 0 then the num to add
            data.append(0)
            data.append(int(splitted[1]))
        line = file.readline().strip()
    return data


def part_one(data):
    # find sum of six signal strengths: 20,40,...220
    index, counter = 1, 20
    curr, total = 1, 0
    for num in data:
        if index == counter:
            print("curr: {}, counter = {}".format(curr, counter))
            total += curr * counter
            counter += 40
        curr += num
        index += 1
    return total


def part_two(data):
    # find CRT image
    rows, cols = 6, 40
    matrix = [["." for i in range(cols)] for j in range(rows)]
    row = index = 0
    sprite = 1

    def mark_CRT():
        if abs(sprite - index) <= 1:
            matrix[row][index] = "#"

    for num in data:
        # update matrix based on sprite position
        mark_CRT()
        sprite += num
        index += 1
        if index == cols:
            # update the row
            row += 1
            index = 0
    return matrix


if __name__ == "__main__":
    data = parse_input()
    print(part_one(data))
    matrix = part_two(data)
    for row in matrix:
        print(row)
