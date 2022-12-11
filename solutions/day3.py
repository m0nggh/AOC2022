def parse_input():
    data = []
    file = open("inputs/day3.txt", "r")
    line = file.readline().strip()
    while line != '':
        data.append(line)
        line = file.readline().strip()
    # final data format: ['aaa', 'AAA']
    return data


def calculate_priority(ch):
    score = 0
    if ch.isupper():
        score += 26  # add for capital letter first
        ch = ch.lower()
    score += ord(ch) - ord('a') + 1  # comapre lower letter
    return score


def part_one(data):
    # calculate sum of priorities
    total = 0
    for row in data:
        n = len(row)
        first, second = row[:n//2], row[n//2:]
        s = set(first)
        # check second with first set for the common occurrence
        common = ''
        for ch in second:
            if ch in s:
                common = ch
                break
        total += calculate_priority(common)
    return total


def part_two(data):
    # calculate priorities for groups of 3
    total = 0
    for i in range(0, len(data), 3):
        m = {}  # use a map to store the count of the letters
        for j in range(3):
            for ch in data[i + j]:
                # only add unique count
                if m.get(ch, 0) == j:
                    m[ch] = m.get(ch, 0) + 1
        # find the common letter
        common = ''
        for ch, count in m.items():
            if count == 3:
                common = ch
                break
        total += calculate_priority(common)
    return total


if __name__ == "__main__":
    data = parse_input()
    # print(data)
    print(part_one(data))
    print(part_two(data))
