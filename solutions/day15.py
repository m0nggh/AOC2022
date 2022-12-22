def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def parse_input():
    sensors, beacons = set(), set()
    file = open("inputs/day15.txt", "r")
    line = file.readline().strip()
    while line != "":
        splitted = line.split()
        sx, sy = int(splitted[2][2:-1]), int(splitted[3][2:-1])
        bx, by = int(splitted[8][2:-1]), int(splitted[9][2:])
        dist = calculate_manhattan_distance(sx, sy, bx, by)
        sensors.add((sx, sy, dist))
        beacons.add((bx, by))
        line = file.readline().strip()
    return sensors, beacons


def can_place_beacon(x, y, beacons):
    for sx, sy, dist in sensors:
        if calculate_manhattan_distance(x, y, sx, sy) <= dist and (x, y) not in beacons:
            return False
    return True


def part_one(sensors, beacons):
    # calculate number of positions a beacon cannot be placed at 2000000
    '''
    calculate the range of x-values for the row which are of manhattan distance from any sensor
    remember to not include beacons!
    '''
    y = 2000000
    total = 0
    for x in range(min(x - d for x, _, d in sensors), max(x + d for x, _, d in sensors)):
        if not can_place_beacon(x, y) and (x, y) not in beacons:
            total += 1
    return total


def part_two(sensors, beacons):
    '''
    very important: since there is only one unique point: it has to be at the intersection 
    of the boundaries of squares, so only start search the boundary
    '''
    boundary = 4000000
    for sx, sy, dist in sensors:
        for dx in range(dist + 2):
            dy = dist + 1 - dx
            for mx, my in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                x, y = sx + (dx * mx), sy + (dy * my)
                if x < 0 or x >= boundary or y < 0 or y >= boundary:
                    continue
                if can_place_beacon(x, y, beacons):
                    return x * boundary + y
    return -1


if __name__ == "__main__":
    sensors, beacons = parse_input()
    print(part_one(sensors, beacons))
    print(part_two(sensors, beacons))
