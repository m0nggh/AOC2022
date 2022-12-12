def parse_input():
    data = []
    with open("inputs/day5.txt", "r") as file:
        data = file.read().split("\n\n")
    crates, instructions = data[0].split("\n"), data[1].split("\n")
    instructions.pop()  # remove empty line

    def parse_crates():
        col_info = crates[-1]  # "1 2 3 "
        cols = int(col_info.strip()[-1])
        crates.pop()  # remove col info
        rows = len(crates)
        stacks = [[] for i in range(cols)]

        # parse the crates into stacks from the bottom
        for r in range(rows - 1, -1, -1):
            row = crates[r]
            for c, ch in enumerate(row):
                if ch.isalpha():
                    # use the col index and info to find the correct col
                    # adjust 1-index to 0-index
                    correct_col = int(col_info[c]) - 1
                    stacks[correct_col].append(ch)
        return stacks

    def parse_instructions():
        # instruction: move 1 from 2 to 1
        final_instructions = []  # format: [quantity, from, to]
        for instruction in instructions:
            inst_list = instruction.split()
            trio = [int(inst_list[1]), int(inst_list[3]) - 1,
                    int(inst_list[5]) - 1]  # adjust 1-index to 0-index
            final_instructions.append(trio)
        return final_instructions

    return (parse_crates(), parse_instructions())


def execute_instruction_part_one(instruction, crates):
    qty, start, end = instruction[0], instruction[1], instruction[2]
    while qty > 0:
        crates[end].append(crates[start].pop())
        qty -= 1


def part_one(crates, instructions):
    # return top of each stack, cratemover does it one by one
    for instruction in instructions:
        execute_instruction_part_one(instruction, crates)
    return ''.join([stack[-1] for stack in crates])


def execute_instruction_part_two(instruction, crates):
    qty, start, end = instruction[0], instruction[1], instruction[2]
    temp = []
    while qty > 0:
        temp.append(crates[start].pop())
        qty -= 1
    while temp:
        # pop it to maintain order
        crates[end].append(temp.pop())


def part_two(crates, instructions):
    # return top of each stack, cratemover does it as a batch
    for instruction in instructions:
        execute_instruction_part_two(instruction, crates)
    return ''.join([stack[-1] for stack in crates])


if __name__ == "__main__":
    crates, instructions = parse_input()
    # print(part_one(crates, instructions))
    print(part_two(crates, instructions))
