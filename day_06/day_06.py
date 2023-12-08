import math
import os
from adventofcodeutils import measure_time, get_numbers_in_string
from aoc_challenge import AocChallenge


def quadratic_equation_solve(time, distance):
    return (math.ceil((time / 2) - math.sqrt((time / 2) ** 2 - (distance +1))),
            math.floor((time / 2) + math.sqrt((time / 2) ** 2 - (distance + 1))))


@measure_time
def stars(starnumber: int, data: list):
    if starnumber == 1:
        records = get_numbers_in_string(data[1])
        final_count = 1
        for i, duration in enumerate(get_numbers_in_string(data[0])):
            # Find the range of the hold time that beat the record
            x1, x2 = quadratic_equation_solve(duration, records[i])
            final_count *= (x2 - x1 + 1)
        return final_count
    elif starnumber == 2:
        # Find the range of the hold time that beat the record
        x1, x2 = quadratic_equation_solve(get_numbers_in_string(data[0].replace(' ', ''))[0],
                                          get_numbers_in_string(data[1].replace(' ', ''))[0])
        return x2 - x1 + 1


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 288, 71503, stars)


if __name__ == "__main__":
    main()
