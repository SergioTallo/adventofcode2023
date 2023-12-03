import os

from adventofcodeutils import aoc_challenge


def stars(starnumber: int, inputfile: str):
    pass


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cookie_file_path = os.path.join(parent_directory, 'session_cookie.txt')

    challenge_4 = aoc_challenge(day, 2023, cookie_file_path)

    challenge_4.test(stars(1, 'test.txt'),
                     stars(2, 'test.txt'),
                     None, None)

    challenge_4.challenge(stars(1, f'input_day{day}.txt'),
                          stars(2, f'input_day{day}.txt'))


if __name__ == "__main__":
    main()
