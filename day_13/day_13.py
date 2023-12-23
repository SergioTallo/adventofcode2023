import os
from adventofcodeutils import measure_time, get_blocks, transform_to_list
from aoc_challenge import AocChallenge


def check_differences(line1: list, line2: list) -> int:
    differences = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            differences += 1
    return differences


def check_horizontal_lines(data: list, max_difference: int) -> int:
    new_max_difference = max_difference
    for i in range(len(data) - 1):
        if check_differences(data[i], data[i + 1]) <= max_difference:
            if check_differences(data[i], data[i + 1]) != 0:
                new_max_difference = 0
            j = 0
            while i + j + 1 <= len(data) - 1 and i - j >= 0:
                if check_differences(data[i - j], data[i + j + 1]) > new_max_difference:
                    new_max_difference = max_difference
                    break
                if check_differences(data[i - j], data[i + j + 1]) != 0:
                    new_max_difference = max_difference
                j += 1
            else:
                return i + 1
    return 0


@measure_time
def stars(starnumber: int, data: list):
    max_difference = 0
    if starnumber == 1:
        max_difference = 0
    elif starnumber == 2:
        max_difference = 1

    blocks = get_blocks(data)
    total = 0
    for i, block in enumerate(blocks):
        old_total = total
        block_horizontal = transform_to_list(block)
        total += check_horizontal_lines(block_horizontal, max_difference) * 100
        if total == old_total:
            block_vertical = [list(row) for row in zip(*block_horizontal)]
            total += check_horizontal_lines(block_vertical, max_difference)
    return total


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 405, 400, stars)


if __name__ == "__main__":
    main()
