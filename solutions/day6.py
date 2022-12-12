def parse_input():
    file = open("inputs/day6.txt", "r")
    line = file.readline().strip()
    return line


def sliding_window(data, window_size):
    # find first start-of-packet marker, sets of window size
    # use sliding window, with a character array
    char_arr = [0] * 26
    unique_count = 0
    # gather first window-size number of letters first
    for i in range(window_size - 1):
        idx = ord(data[i]) - ord('a')
        if char_arr[idx] == 0:
            unique_count += 1
        char_arr[idx] += 1

    # perform sliding window
    for i in range(window_size - 1, len(data)):
        # add last letter
        idx = ord(data[i]) - ord('a')
        if char_arr[idx] == 0:
            unique_count += 1
        char_arr[idx] += 1

        # check if it is a marker
        if unique_count == window_size:
            return i + 1  # adjust 0-index to 1-index

        # remove first letter
        first_idx = ord(data[i - window_size + 1]) - ord('a')
        if char_arr[first_idx] == 1:
            unique_count -= 1
        char_arr[first_idx] -= 1
    return -1  # not possible


def part_one(data):
    return sliding_window(data, 4)


def part_two(data):
    return sliding_window(data, 14)


if __name__ == "__main__":
    data = parse_input()
    # print(data)
    print(part_one(data))
    print(part_two(data))
