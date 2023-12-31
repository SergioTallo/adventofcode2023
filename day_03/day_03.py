import os
from functools import reduce

from adventofcodeutils import get_neighbors, measure_time
from aoc_challenge import AocChallenge


def check_neighbors(data: list, x: int, y: int, gear):
    gear_found = False
    gear_coord = (0, 0)

    neighbors_ = get_neighbors(data, x, y, True)
    neighbors = neighbors_[0]
    coord_neighbors = neighbors_[1]

    for neighbor in neighbors:
        if neighbor != '.' and not neighbor.isdigit() and not neighbor.isalpha():
            if not gear:
                return True
            else:
                if neighbor == '*':
                    gear_found = True
                    gear_coord = coord_neighbors[neighbor]
                    return gear_found, gear_coord
    if gear:
        return gear_found, gear_coord
    else:
        return False


def append_number(nexto: bool, gear_bool: bool, gear_coord: tuple, starnumber: int, number: str,
                  numbers_line: list, numbers_gears: dict):
    if nexto:
        numbers_line.append(int(number))
        if starnumber == 2:
            if gear_bool:
                if gear_coord not in numbers_gears:
                    numbers_gears[gear_coord] = [int(number)]
                else:
                    numbers_gears[gear_coord].append(int(number))


def score_for_star_2(numbers_gears: dict):
    # Filter out the gears that have only one number
    keys_with_two_unique_values = {key for key, values in numbers_gears.items() if len(values) == 2}
    numbers_gears = {key: value for key, value in numbers_gears.items() if key in keys_with_two_unique_values}

    # Compute the individual ratio of each gear and sum them up
    score = 0
    for key, value in numbers_gears.items():
        score += reduce((lambda x, y: x * y), value)
    return score

@measure_time
def stars(starnumber: int, data: list):
    numbers_line = []
    numbers_gears = {}
    for i, line in enumerate(data):
        number = ''
        nexto = False
        gear_bool = False
        gear_coord = (0, 0)
        for j, char in enumerate(line):
            if char.isdigit():
                number += char
                if not nexto:
                    nexto = check_neighbors(data, j, i, False)
                if starnumber == 2:
                    if not gear_bool:
                        check = check_neighbors(data, j, i, True)
                        gear_bool = check[0]
                        gear_coord = check[1]
            elif data[i][j - 1].isdigit():
                append_number(nexto, gear_bool, gear_coord, starnumber, number, numbers_line, numbers_gears)
                number = ''
                nexto = False
                gear_bool = False
                gear_coord = (0, 0)

        # Take of the special care if the number is at the end of the line
        if data[i][len(line) - 1].isdigit():
            append_number(nexto, gear_bool, gear_coord, starnumber, number, numbers_line, numbers_gears)

    if starnumber == 1:
        return sum(numbers_line)

    elif starnumber == 2:
        return score_for_star_2(numbers_gears)


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 4361, 467835, stars)


if __name__ == "__main__":
    main()
