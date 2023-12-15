import os
from adventofcodeutils import measure_time
from aoc_challenge import AocChallenge


def calculate_hash(code: str) -> int:
    hash_code = 0
    for char in code:
        hash_code += ord(char)
        hash_code *= 17
        hash_code %= 256
    return hash_code


def calculate_lens(code: str) -> tuple:
    if '=' in code:
        return calculate_hash(code.split('=')[0]), code.split('=')[0], 0, int(code.split('=')[1])
    elif '-' in code:
        return calculate_hash(code.split('-')[0]), code.split('-')[0], 1, 0


def initialize_lens_box(number_lenses: int) -> dict:
    lens_box = {}
    for i in range(number_lenses):
        lens_box[i] = {}
    return lens_box


def calculate_focus_power(lens_box: dict) -> int:
    focus_power = 0
    for box in lens_box:
        for i, lens in enumerate(lens_box[box]):
            focus_power += (box + 1) * (i + 1) * lens_box[box][lens]
    return focus_power


def place_lens(lens_box: dict, code: str) -> dict:
    box, label, lens_type, focal_length = calculate_lens(code)
    if lens_type == 0:
        lens_box[box][label] = focal_length
    elif lens_type == 1:
        if label in lens_box[box]:
            lens_box[box].pop(label)
    return lens_box


@measure_time
def stars(starnumber: int, data: list):
    if starnumber == 1:
        alg_value = 0
        for code in data[0].split(','):
            alg_value += calculate_hash(code)
        return alg_value
    elif starnumber == 2:
        lens_box = initialize_lens_box(256)
        for code in data[0].split(','):
            lens_box = place_lens(lens_box, code)
        return calculate_focus_power(lens_box)


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 1320, 145, stars)


if __name__ == "__main__":
    main()
