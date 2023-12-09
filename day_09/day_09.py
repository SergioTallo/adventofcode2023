import os
from adventofcodeutils import measure_time, get_numbers_in_string
from aoc_challenge import AocChallenge


def generate_sequence(starting_sequence: list) -> list:
    new_sequence = []
    for i in range(len(starting_sequence)):
        if i < len(starting_sequence) - 1:
            new_sequence.append(starting_sequence[i + 1] - starting_sequence[i])
    return new_sequence


def extrapolated_value(original_sequence: list) -> int:
    if all(element == 0 for element in original_sequence):
        return 0
    else:
        value = extrapolated_value(generate_sequence(original_sequence))
        return original_sequence[-1] + value


@measure_time
def stars(starnumber: int, data: list):
    if starnumber == 1:
        return sum([extrapolated_value(get_numbers_in_string(line)) for line in data])
    elif starnumber == 2:
        return sum([extrapolated_value(get_numbers_in_string(line)[::-1]) for line in data])


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 114, 2, stars)


if __name__ == "__main__":
    main()
