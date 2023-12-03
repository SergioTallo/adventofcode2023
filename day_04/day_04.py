import os

from adventofcodeutils import aoc_challenge


def stars(starnumber: int, inputfile: str):
    pass


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    aoc_challenge(day, 2023, None, None, stars)


if __name__ == "__main__":
    main()
