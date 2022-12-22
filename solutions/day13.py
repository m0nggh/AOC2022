from functools import cmp_to_key
index = 1  # for parsing the list of lists


def parse_input():
    global index
    pairs = []
    file = open("inputs/day13.txt", "r")
    first = file.readline().strip()

    def parse_line_into_array(line):
        global index
        res = []
        while index < len(line):
            ch = line[index]
            # 3 cases for items in the res list
            if ch == "[":
                # case 1: recurse and append another list as an element
                index += 1
                res.append(parse_line_into_array(line))
            elif ch == "]":
                # case 2: closing bracket found, exit recursion
                break
            elif ch.isdigit():
                # case 3: numbers, need to accummulate the digits
                curr_no = 0
                while ch.isdigit():
                    curr_no = curr_no * 10 + int(ch)
                    index += 1
                    ch = line[index]
                res.append(curr_no)
                index -= 1  # reset back
            index += 1
        return res

    while first != "":
        second = file.readline().strip()
        first_list = parse_line_into_array(first)
        index = 1  # reset the index
        second_list = parse_line_into_array(second)
        index = 1  # reset the index
        pairs.append((first_list, second_list))
        file.readline()  # buffer line between pairs
        first = file.readline().strip()
    return pairs


def part_one(pairs):
    # find sum of indices of pairs in the right order
    total = pair_index = 0

    def is_pair_in_order(list1, list2):
        index1 = index2 = 0
        len1, len2 = len(list1), len(list2)
        while index1 < len1 and index2 < len2:
            item1, item2 = list1[index1], list2[index2]
            # recurse item as sublist if required
            if isinstance(item1, list) or isinstance(item2, list):
                if isinstance(item1, int):
                    item1 = [item1]
                if isinstance(item2, int):
                    item2 = [item2]
                # only a wrong pair of sublist has to be penalised
                is_sub_pair_in_order = is_pair_in_order(item1, item2)
                if is_sub_pair_in_order is not None:
                    return is_sub_pair_in_order
            else:
                # right order: left item smaller than right item
                if item1 < item2:
                    return True
                # wrong order: left item larger than right item
                elif item1 > item2:
                    return False

            # continue looking at other elements if equal
            index1 += 1
            index2 += 1

        # final check: right order only if index1 == len1 (left ran out of items first)
        return None if index1 == len1 and index2 == len2 else index1 == len1

    for pair in pairs:
        list1, list2 = pair[0], pair[1]
        if is_pair_in_order(list1, list2):
            total += pair_index + 1  # accummulate as 1-index
        pair_index += 1
    return total


def pair_cmp(list1, list2):
    # right order return -1 cus "smaller", wrong order return 1
    index1 = index2 = 0
    len1, len2 = len(list1), len(list2)
    while index1 < len1 and index2 < len2:
        item1, item2 = list1[index1], list2[index2]
        # recurse item as sublist if required
        if isinstance(item1, list) or isinstance(item2, list):
            if isinstance(item1, int):
                item1 = [item1]
            if isinstance(item2, int):
                item2 = [item2]
            # only a wrong pair of sublist has to be penalised
            is_sub_pair_in_order = pair_cmp(item1, item2)
            if is_sub_pair_in_order != 0:
                return is_sub_pair_in_order
        else:
            # right order: left item smaller than right item
            if item1 < item2:
                return -1
            # wrong order: left item larger than right item
            elif item1 > item2:
                return 1

        # continue looking at other elements if equal
        index1 += 1
        index2 += 1

    # final check: right order only if index1 == len1 (left ran out of items first)
    if index1 == len1 and index2 == len2:
        return 0
    elif index1 == len1:
        return -1
    return 1


def part_two(pairs):
    # locate the two divider packets
    packets = [[2], [6]]
    for pair in pairs:
        packets.extend([pair[0], pair[1]])
    packets.sort(key=cmp_to_key(pair_cmp))
    divider_packet_1 = divider_packet_2 = 0
    for i in range(len(packets)):
        packet = packets[i]
        if len(packet) == 1:
            if packet[0] == 2:
                divider_packet_1 = i + 1  # 1-index
            if packet[0] == 6:
                divider_packet_2 = i + 1  # 1-index
    # print(divider_packet_1, divider_packet_2)
    return divider_packet_1 * divider_packet_2


if __name__ == "__main__":
    data = parse_input()
    # for pair in data:
    #     print(pair)
    print(part_one(data))
    print(part_two(data))
