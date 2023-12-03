from functools import reduce
from adventofcodeutils import readlines, get_neighbors


def check_neighbors(data: list, x: int, y: int, gear):
    gear_found = False
    gear_coord = (0, 0)
    coord_neighbors = {}

    if gear:
        neighbors_ = get_neighbors(data, x, y, True)
        neighbors = neighbors_[0]
        coord_neighbors = neighbors_[1]
    else:
        neighbors = get_neighbors(data, x, y, False)

    for neighbor in neighbors:
        if neighbor != '.' and not neighbor.isdigit() and not neighbor.isalpha():
            if not gear:
                return True
        if neighbor == '*':
            gear_found = True
            gear_coord = coord_neighbors[neighbor]

    if gear:
        return gear_found, gear_coord
    return False


def calculate_value_of_gears(gears):
    pass


def stars(starnumber: int, inputfile: str):
    data = readlines(inputfile)

    numbers_line = []
    numbers_gears = {}
    for i, line in enumerate(data):
        number = ''
        number_bool = False
        nexto = False
        gear_bool = False
        gear_coord = (0, 0)
        for j, char in enumerate(line):
            if char.isdigit():
                number += char
                number_bool = True
                if not nexto:
                    nexto = check_neighbors(data, j, i, False)
                if starnumber == 2:
                    if not gear_bool:
                        check = check_neighbors(data, j, i, True)
                        if check[0]:
                            gear_bool = True
                            gear_coord = check[1]

                # Take of the special care if the number is at the end of the line
                if j == len(line) - 1:
                    if number_bool and nexto:
                        numbers_line.append(int(number))
                        if starnumber == 2:
                            if gear_bool:
                                if gear_coord not in numbers_gears:
                                    numbers_gears[gear_coord] = []
                                numbers_gears[gear_coord].append(int(number))
                    number = ''
                    number_bool = False
                    nexto = False
                    gear_bool = False
                    gear_coord = (0, 0)
            else:
                if number_bool:
                    if nexto:
                        numbers_line.append(int(number))
                    if starnumber == 2:
                        if gear_bool:
                            if gear_coord not in numbers_gears:
                                numbers_gears[gear_coord] = []
                            numbers_gears[gear_coord].append(int(number))

                    number = ''
                    number_bool = False
                    nexto = False
                    gear_bool = False
                    gear_coord = (0, 0)
    if starnumber == 1:
        return sum(numbers_line)
    elif starnumber == 2:
        # Filter out the gears that have only one number
        keys_with_two_unique_values = {key for key, values in numbers_gears.items() if len(values) == 2}
        numbers_gears = {key: value for key, value in numbers_gears.items() if key in keys_with_two_unique_values}

        # Compute the individual ratio of each gear and sum them up
        score = 0
        for key, value in numbers_gears.items():
            score += reduce((lambda x, y: x * y), value)
        return score


assert stars(1, 'test.txt') == 4361, "Star one failed, should be 4361"
print(f"Score 1: {stars(1, 'input.txt')}")
assert stars(2, 'test.txt') == 467835, "Star two failed, should be 467835"
print(f"Score 2: {stars(2, 'input.txt')}")