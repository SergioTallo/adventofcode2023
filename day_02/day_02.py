from adventofcodeutils import readlines, download_input, aoc_challenge
import os
import re
from functools import reduce
from operator import mul


def check_color_count(matches: list, id):
    predefined_counts = {'red': 12, 'green': 13, 'blue': 14}
    for count, color in matches:
        count = int(count)
        if color in predefined_counts and count > predefined_counts[color]:
            return 0
    return id


def check_min_count(matches: list):
    color_counts = {}
    for count, color in matches:
        if color not in color_counts or int(count) > color_counts[color]:
            color_counts[color] = int(count)
    if len(color_counts) < 3:
        return 0
    else:
        return reduce(mul, color_counts.values(), 1)


def stars(number, input):
    score = 0
    data = readlines(input)
    for game in data:
        pattern = r'(\d+)\s(\w+)'
        id, sets = int(game.split(':')[0].split(' ')[1].strip()), game.split(':')[1].strip()
        matches = re.findall(pattern, sets)
        if number == 1:
            score += check_color_count(matches, id)
        elif number == 2:
            score += check_min_count(matches)
    return score

def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    challenge_2 = aoc_challenge(day, 2023)

    challenge_2.test(stars(1, 'test.txt'),
                     stars(2, 'test.txt'),
                     8, 2286)

    challenge_2.challenge(stars(1, f'input_day{day}.txt'),
                          stars(2, f'input_day{day}.txt'))


if __name__ == "__main__":
    main()
