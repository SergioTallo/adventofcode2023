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
    subsequence_sequences = [original_sequence]
    new_sequence = generate_sequence(original_sequence)
    subsequence_sequences.append(new_sequence)
    # Generate the piramide
    while not all(element == 0 for element in new_sequence):
        new_sequence = generate_sequence(new_sequence)
        subsequence_sequences.append(new_sequence)

    # Calculate the value of the new element
    x = 0
    if all(element == 0 for element in new_sequence) and len(new_sequence) > 1:
        for i in range(len(subsequence_sequences)):
            x += subsequence_sequences[i][-1]
    return x


@measure_time
def stars(starnumber: int, data: list):
    if starnumber == 1:
        new_numbers = []
        for i, line in enumerate(data):
            new_numbers.append(extrapolated_value(get_numbers_in_string(line)))
        return sum(new_numbers)
    elif starnumber == 2:
        new_numbers = []
        for i, line in enumerate(data):
            new_numbers.append(extrapolated_value(get_numbers_in_string(line)[::-1]))
        return sum(new_numbers)


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 114, 2, stars)


if __name__ == "__main__":
    main()
