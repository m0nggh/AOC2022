# assume a 1000 x 1000 board since the size is not given
SIZE = 1000
START = 500


def parse_input():
    data = []
    file = open("inputs/day9.txt", "r")
    line = file.readline().strip()
    while line != '':
        splitted = line.split()
        data.append((splitted[0], int(splitted[1])))  # direction + steps
        line = file.readline().strip()
    return data


def should_move_tail(r1, c1, r2, c2):
    return abs(r1 - r2) > 1 or abs(c1 - c2) > 1


def part_one(data):
    # find number of unique tail positions
    visited = [[False for i in range(SIZE)] for j in range(SIZE)]
    # start from the centre
    dirs = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
    head_row = head_col = START
    tail_row, tail_col = head_row, head_col
    visited[tail_row][tail_col] = True
    for line in data:
        direction, steps = line[0], line[1]
        movement = dirs[direction]
        while steps > 0:
            new_row, new_col = head_row + movement[0], head_col + movement[1]
            if should_move_tail(tail_row, tail_col, new_row, new_col):
                visited[head_row][head_col] = True  # tag tail in old position
                tail_row, tail_col = head_row, head_col  # move tail to prev head position
            head_row, head_col = new_row, new_col  # move head
            steps -= 1
    return sum([sum(row) for row in visited])


# THIS IS FOR PART 2
def move(r1, c1, r2, c2):
    # move straight if head and tail are on the same row or col
    if abs(r1 - r2) == 0 or abs(c1 - c2) == 0:
        return move_straight(r1, c1, r2, c2)
    return move_diagonally(r1, c1, r2, c2)


def move_straight(r1, c1, r2, c2):
    # r1, c1 --> from, r2, c2 --> to
    # try all four directions
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for direction in dirs:
        new_r, new_c = r1 + direction[0], c1 + direction[1]
        # check if it is in range
        if new_r < 0 or new_r >= SIZE or new_c < 0 or new_c >= SIZE:
            continue
        if not should_move_tail(new_r, new_c, r2, c2):
            return (new_r, new_c)  # only one possible direction
    return None  # not possible


def move_diagonally(r1, c1, r2, c2):
    # r1, c1 --> from, r2, c2 --> to
    # try all four directions
    dirs = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    for direction in dirs:
        new_r, new_c = r1 + direction[0], c1 + direction[1]
        # check if it is in range
        if new_r < 0 or new_r >= SIZE or new_c < 0 or new_c >= SIZE:
            continue
        if not should_move_tail(new_r, new_c, r2, c2):
            return (new_r, new_c)  # only one possible direction
    return None  # not possible


def part_two(data):
    # extend tail to 9 units long
    # assume a 1000 x 1000 board since the size is not given
    visited = [[False for i in range(SIZE)] for j in range(SIZE)]
    # start from the centre
    dirs = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
    # create an array to store its own head and tail row/col
    # [row, col] for size 9, first index is no 1, last index is the tail (no 9)
    # head_row = head_col = 50
    head_row = head_col = START
    positions = [[head_row, head_col] for i in range(9)]
    visited[head_row][head_col] = True
    for line in data:
        direction, steps = line[0], line[1]
        movement = dirs[direction]
        while steps > 0:
            # check and update the first index of positions
            # move head row and head col
            new_row, new_col = head_row + movement[0], head_col + movement[1]
            index = 0
            if should_move_tail(positions[index][0], positions[index][1], new_row, new_col):
                # update the first index position
                positions[index][0], positions[index][1] = move(
                    positions[index][0], positions[index][1], new_row, new_col)

                # do chain reaction down
                index += 1
                while index < 9 and should_move_tail(positions[index][0], positions[index][1], positions[index - 1][0], positions[index - 1][1]):
                    # update new position
                    positions[index][0], positions[index][1] = move(
                        positions[index][0], positions[index][1], positions[index - 1][0], positions[index - 1][1])
                    index += 1

                if index == 9:
                    # the tail moved, so tag the tail's new position it moved to
                    visited[positions[index - 1][0]
                            ][positions[index - 1][1]] = True
            head_row, head_col = new_row, new_col  # move head
            steps -= 1
    return sum([sum(row) for row in visited])


if __name__ == "__main__":
    data = parse_input()
    print(part_one(data))
    print(part_two(data))
