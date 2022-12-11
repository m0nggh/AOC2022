def parse_input():
    data = []
    with open("inputs/day2.txt", "r") as file:
        data = file.read().split("\n")  # split by lines
    data.pop()  # remove last empty line
    # final data format: ['A X', 'B Y']
    return data


def part_one(data, points_arr, score_matrix):
    # calculate strategy points
    total = 0
    for row in data:
        opp, player = row.split()
        opp_index, player_index = ord(opp) - ord('A'), ord(player) - ord('X')
        total += score_matrix[opp_index][player_index] + \
            points_arr[player_index]
    return total


def part_two(data, points_arr, score_matrix):
    # x: lose, y: draw, z: win
    total = 0
    for row in data:
        opp, outcome = row.split()
        opp_index, outcomeIndex = ord(opp) - ord('A'), ord(outcome) - ord('X')
        point_to_search_for = outcomeIndex * 3  # 0,3 or 6
        player_index = 0  # rock by default first
        # search the through the row in the score matrix for the corresponding player_index move
        for i in range(3):
            if score_matrix[opp_index][i] == point_to_search_for:
                player_index = i
        total += point_to_search_for + points_arr[player_index]
    return total


if __name__ == "__main__":
    data = parse_input()
    points_arr = [1, 2, 3]  # rock, paper, scissors
    score_matrix = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]
    # print(data)
    print(part_one(data, points_arr, score_matrix))
    print(part_two(data, points_arr, score_matrix))
