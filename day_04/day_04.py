import os
from adventofcodeutils import aoc_challenge, measure_time


@measure_time
def stars(starnumber: int, data: list):
    if starnumber == 1:
        pass
    elif starnumber == 2:
        pass


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    aoc_challenge(day, 2023, None, None, stars)


if __name__ == "__main__":
    main()
