import os
from adventofcodeutils import measure_time, get_numbers_in_string, transform_to_list
from aoc_challenge import AocChallenge


def num_of_arrangements(line: str) -> int:
    field = list(line.split(' ')[0])
    instructions = get_numbers_in_string(line.split(' ')[1])
    return calculate_arrangements(field, instructions, 0)[2]


def calculate_arrangements(field: list, instructions: list, correct_arrangements: 0) -> tuple:
    print(field, instructions, correct_arrangements)
    if len(field) == 0 and len(instructions) == 0:
        print('no instructions left')
        return [], [], correct_arrangements + 1
    if len(field) == 0:
        print('no field left')
        print(instructions)
        return [], [], correct_arrangements

    if field[0] == '.':
        return calculate_arrangements(field[1:], instructions, correct_arrangements)

    if field[0] == '#':
        if len(instructions) == 0:
            return [], [], correct_arrangements
        if instructions[0] > len(field):
            return [], [], correct_arrangements
        for i in range(instructions[0]):
            if field[i] == '.':
                return [], [], correct_arrangements
        if instructions[0] == len(field):
            return calculate_arrangements([], instructions[1:], correct_arrangements)
        if field[instructions[0]] == '#':
            return calculate_arrangements([], [], correct_arrangements)

        return calculate_arrangements(field[instructions[0] +1:], instructions[1:], correct_arrangements)

    if field[0] == '?':
        if len(instructions) == 0:
            return calculate_arrangements(field[1:], instructions, correct_arrangements)
        if instructions[0] > len(field):
            return [], [], correct_arrangements
        for i in range(instructions[0]):
            if field[i] == '.':
                return correct_arrangements(field[i:], instructions, correct_arrangements)
        if instructions[0] == len(field):
            return calculate_arrangements([], instructions[1:], correct_arrangements)
        if field[instructions[0]] == '#':
            return calculate_arrangements([], [], correct_arrangements)

        return calculate_arrangements(field[instructions[0] + 1:], instructions[1:], correct_arrangements)


@measure_time
def stars(starnumber: int, data: list):
    pass


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, None, None, stars)


if __name__ == "__main__":
    main()
