def parse_input():
    matrix = []
    file = open("inputs/day8.txt", "r")
    line = file.readline().strip()
    while line != '':
        row = []
        for ch in line:
            row.append(int(ch))
        matrix.append(row)
        line = file.readline().strip()
    return matrix


def check_visibility(matrix, row, col, x, y):
    rows, cols = len(matrix), len(matrix[0])
    curr = matrix[row][col]
    row, col = row + x, col + y
    while row >= 0 and row < rows and col >= 0 and col < cols:
        if matrix[row][col] >= curr:
            return False
        row, col = row + x, col + y
    return True


def part_one(matrix):
    # find visible trees
    rows, cols = len(matrix), len(matrix[0])
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    total = 0
    # trace and check matrix from all four directions
    for row in range(rows):
        for col in range(cols):
            for direction in dirs:
                x, y = direction[0], direction[1]
                if check_visibility(matrix, row, col, x, y):
                    total += 1
                    break
    return total


def calculate_distance(matrix, row, col, x, y):
    rows, cols = len(matrix), len(matrix[0])
    curr = matrix[row][col]
    row, col = row + x, col + y
    curr_dist = 0
    while row >= 0 and row < rows and col >= 0 and col < cols:
        curr_dist += 1
        if matrix[row][col] >= curr:
            return curr_dist
        row, col = row + x, col + y
    return curr_dist


def part_two(matrix):
    # find max scenic score
    rows, cols = len(matrix), len(matrix[0])
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    max_scenic_score = 0
    # trace and calculate highest score from all four directions
    for row in range(rows):
        for col in range(cols):
            curr_scenic_score = 1
            for direction in dirs:
                x, y = direction[0], direction[1]
                dist = calculate_distance(matrix, row, col, x, y)
                if dist == 0:
                    curr_scenic_score = 0  # invalid
                    break
                curr_scenic_score *= dist
            max_scenic_score = max(
                max_scenic_score, curr_scenic_score)  # update max
    return max_scenic_score


if __name__ == "__main__":
    data = parse_input()
    print(part_one(data))
    print(part_two(data))
