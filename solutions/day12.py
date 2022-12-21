from collections import deque

ROWS = 0
COLS = 0


def parse_input():
    global ROWS, COLS
    matrix = []
    file = open("inputs/day12.txt", "r")
    line = file.readline().strip()
    while line != "":
        curr_row = []
        for ch in line:
            curr_row.append(ch)
        matrix.append(curr_row)
        line = file.readline().strip()
    ROWS, COLS = len(matrix), len(matrix[0])
    return matrix


def part_one(matrix):
    # find fewest steps from a fixed starting position: bfs
    end_row = end_col = 0
    queue = deque()
    visited = [[False for i in range(COLS)] for j in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            ch = matrix[i][j]
            if ch == "S":
                matrix[i][j] = "a"
                queue.append((i, j))
                visited[i][j] = True
            elif ch == "E":
                matrix[i][j] = "z"
                end_row, end_col = i, j

    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    level = 0
    while queue:
        size = len(queue)
        while size > 0:
            curr = queue.popleft()
            x, y = curr[0], curr[1]
            curr_ch = matrix[x][y]
            # search neighbours
            for direction in dirs:
                x1, y1 = x + direction[0], y + direction[1]
                # check if in range or visited
                if x1 < 0 or x1 >= ROWS or y1 < 0 or y1 >= COLS or visited[x1][y1]:
                    continue
                next_ch = matrix[x1][y1]
                # if higher level, continue
                if ord(next_ch) > ord(curr_ch) + 1:
                    continue
                # early termination upon seeing end position
                if end_row == x1 and end_col == y1:
                    return level + 1
                queue.append((x1, y1))
                visited[x1][y1] = True
            size -= 1
        level += 1
    return -1  # not possible


def part_two(matrix):
    # find fewest steps from any starting position with "a": bfs
    end_row = end_col = 0
    queue = deque()
    visited = [[False for i in range(COLS)] for j in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            ch = matrix[i][j]
            if visited[i][j]:
                continue
            if ch == "S" or ch == "a":
                matrix[i][j] = "a"  # for "S"
                queue.append((i, j))
                visited[i][j] = True
            elif ch == "E":
                matrix[i][j] = "z"
                end_row, end_col = i, j

    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    level = 0
    while queue:
        size = len(queue)
        while size > 0:
            curr = queue.popleft()
            x, y = curr[0], curr[1]
            curr_ch = matrix[x][y]
            # search neighbours
            for direction in dirs:
                x1, y1 = x + direction[0], y + direction[1]
                # check if in range or visited
                if x1 < 0 or x1 >= ROWS or y1 < 0 or y1 >= COLS or visited[x1][y1]:
                    continue
                next_ch = matrix[x1][y1]
                # if higher level, continue
                if ord(next_ch) > ord(curr_ch) + 1:
                    continue
                # early termination upon seeing end position
                if end_row == x1 and end_col == y1:
                    return level + 1
                queue.append((x1, y1))
                visited[x1][y1] = True
            size -= 1
        level += 1
    return -1  # not possible


if __name__ == "__main__":
    data = parse_input()
    # print(part_one(data))
    print(part_two(data))
