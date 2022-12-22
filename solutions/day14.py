ROWS, COLS = 300, 1000
row, col = 0, 500
last_row = 0


def parse_input():
    global last_row
    matrix = [["." for j in range(COLS)] for i in range(ROWS)]  # default air
    file = open("inputs/day14.txt", "r")
    line = file.readline().strip()
    while line != "":
        coordinates = line.split("->")
        curr_col, curr_row = coordinates[0].strip().split(
            ",")  # given in flipped order
        curr_row, curr_col = int(curr_row), int(curr_col)
        for i in range(1, len(coordinates)):
            coord = coordinates[i]
            next_col, next_row = coord.strip().split(",")  # given in flipped order
            next_row, next_col = int(next_row), int(next_col)
            # mark rocks
            while curr_row != next_row:
                matrix[curr_row][curr_col] = "#"
                curr_row = curr_row + 1 if curr_row < next_row else curr_row - 1
            while curr_col != next_col:
                matrix[curr_row][curr_col] = "#"
                curr_col = curr_col + 1 if curr_col < next_col else curr_col - 1
            matrix[curr_row][curr_col] = "#"  # mark the last one
            last_row = max(last_row, curr_row)  # update base row
            curr_row, curr_col = next_row, next_col  # update with next
        line = file.readline().strip()
    return matrix


def move_one_step(matrix):
    global row, col
    if row == ROWS - 1:
        return False
    # move downwards, diagonal left or diagonal right if possible
    if matrix[row + 1][col] == ".":
        row += 1
        return True
    elif matrix[row + 1][col - 1] == ".":
        row += 1
        col -= 1
        return True
    elif matrix[row + 1][col + 1] == ".":
        row += 1
        col += 1
        return True
    else:
        return False


def part_one(matrix):
    # count units of sand before flowing to abyss below
    global row, col
    while True:
        # simulate sand flow
        while move_one_step(matrix):
            pass
        # check abyss
        if row == ROWS - 1:
            break

        # reset
        matrix[row][col] = "o"  # mark step
        row, col = 0, 500
        total += 1
    return total


def part_two(matrix):
    # count units of sand with horizontal base
    base_row = last_row + 2
    print("base row: {}".format(base_row))
    # fill base row with sand
    for i in range(COLS):
        matrix[base_row][i] = "#"
    global row, col
    total = 1  # include the current start
    while True:
        # simulate sand flow
        count = 0
        while move_one_step(matrix):
            count += 1
        # end condition, no sand is filled
        if count == 0:
            break
        # reset
        matrix[row][col] = "o"  # mark step
        row, col = 0, 500
        total += 1
    return total


if __name__ == "__main__":
    data = parse_input()
    # print(part_one(data))
    print(part_two(data))
