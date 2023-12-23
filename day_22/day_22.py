import os
from adventofcodeutils import measure_time
from aoc_challenge import AocChallenge


@measure_time
def stars(starnumber: int, data: list):
    pass


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, None, None, stars)


if __name__ == "__main__":
    main()
