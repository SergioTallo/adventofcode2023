from readlines import readlines
import re
from functools import reduce
from operator import mul


def check_color_count(matches: list, id, predefined_counts):
    for count, color in matches:
        count = int(count)
        if color in predefined_counts and count > predefined_counts[color]:
            return 0
    return id


def star_one(input, score: int, predefined_counts):
    data = readlines(input)
    for game in data:
        pattern = r'(\d+)\s(\w+)'
        id = int(game.split(':')[0].split(' ')[1].strip())
        sets = game.split(':')[1]
        matches = re.findall(pattern, sets)
        score += check_color_count(matches, id, predefined_counts)
    return score


predefined_counts = {'red': 12, 'green': 13, 'blue': 14}
assert star_one('test.txt', 0, predefined_counts) == 8, "The test score should be 8"

print(f"Score 1: {star_one('input.txt', 0, predefined_counts)}")


def check_min_count(matches: list):
    color_counts = {}
    for count, color in matches:
        if color not in color_counts or int(count) > color_counts[color]:
            color_counts[color] = int(count)
    if len(color_counts) < 3:
        return 0
    else:
        return reduce(mul, color_counts.values(), 1)


def star_two(input, score: int):
    data = readlines(input)
    for game in data:
        pattern = r'(\d+)\s(\w+)'
        sets = game.split(':')[1]
        matches = re.findall(pattern, sets)
        score += check_min_count(matches)
    return score


assert star_two('test.txt', 0) == 2286, "The test score should be 2286"
print(f"Score 2: {star_two('input.txt', 0)}")
