MONKEYS = 8
'''
For an integer n that is divisible by P, then n-kP is also divisible by P. 
You can choose just about anything for k.
To choose k, use LCM of all the divisible numbers because if A % k == 0, where k=x*y*z, A % x/y/z will be 0 also.
'''
SUPERMODULO = 1


class MonkeyFunction:
    def __init__(self, id, operator, operand, divisibility, valid, invalid):
        self.id = id
        self.operator = operator
        self.operand = operand  # if 0, means old * old
        self.divisibility = divisibility
        self.valid = valid
        self.invalid = invalid

    def __str__(self):
        return "Monkey Function {}\n\tOperator: {}\n\tOperand: {}\n\tDivisibility: {}\n\tTrue: monkey {}\n\tFalse: monkey {}\n".format(
            self.id, self.operator, self.operand, self.divisibility, self.valid, self.invalid)


def parse_input():
    global SUPERMODULO
    file = open("inputs/day11.txt", "r")
    items = [[] for i in range(MONKEYS)]
    index = 0
    monkey_functions = []
    for i in range(MONKEYS):
        file.readline()  # monkey number
        items_line = file.readline().strip()
        splitted = items_line.split(" ", 2)  # Starting items: x, y, z...
        # take only the items out
        item_list = splitted[2].split(", ")
        for item in item_list:
            items[index].append(int(item))
        operation = file.readline().strip()
        splitted = operation.split()
        operator = splitted[-2]
        operand = 0 if splitted[-1] == "old" else int(splitted[-1])
        test = file.readline().strip()
        divisibility = int(test.split()[-1])
        valid = int(file.readline().strip()[-1])
        invalid = int(file.readline().strip()[-1])
        monkey_function = MonkeyFunction(
            index, operator, operand, divisibility, valid, invalid)
        monkey_functions.append(monkey_function)
        SUPERMODULO *= divisibility
        file.readline()
        index += 1
    # print(items)
    # print(monkey_functions[0])
    return (items, monkey_functions)


def perform_monkey_business(items, monkey_function, count_arr, part):
    index = monkey_function.id
    item_list = items[index]
    inspect_count = 0
    while item_list:
        inspect_count += 1
        item = item_list.pop()
        # perform operation
        operand = item if monkey_function.operand == 0 else monkey_function.operand
        if monkey_function.operator == "*":
            new_item = item * operand
        else:
            new_item = item + operand
        # monkey bored moment OR supermodulo moment to reduce number
        if part == 1:
            new_item //= 3
        else:
            new_item %= SUPERMODULO
        # check divisibility test
        if new_item % monkey_function.divisibility == 0:
            items[monkey_function.valid].append(new_item)
        else:
            items[monkey_function.invalid].append(new_item)
    count_arr[index] += inspect_count


def part_one(items, monkey_functions):
    # brute force simulation
    rounds = 20
    count_arr = [0] * MONKEYS
    while rounds > 0:
        for i in range(MONKEYS):
            perform_monkey_business(
                items, monkey_functions[i], count_arr, 1)
        rounds -= 1
    sorted_count_arr = sorted(count_arr, reverse=True)
    print(count_arr)
    return sorted_count_arr[0] * sorted_count_arr[1]


def part_two(items, monkey_functions):
    # brute force simulation
    rounds = 10000
    count_arr = [0] * MONKEYS
    while rounds > 0:
        for i in range(MONKEYS):
            perform_monkey_business(
                items, monkey_functions[i], count_arr, 2)
        rounds -= 1
    sorted_count_arr = sorted(count_arr, reverse=True)
    print(count_arr)
    return sorted_count_arr[0] * sorted_count_arr[1]


if __name__ == "__main__":
    items, monkey_functions = parse_input()
    # print(part_one(items, monkey_functions))
    print(part_two(items, monkey_functions))
