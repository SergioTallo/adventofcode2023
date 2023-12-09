import os
from adventofcodeutils import measure_time
from aoc_challenge import AocChallenge
from math import lcm


def create_map(data: list, starnumber: int) -> tuple:
    start_group = []
    steps = {}

    for step in data[2:]:
        step = step.split('=')
        if starnumber == 1:
            if step[0].strip() == 'AAA':
                start_group.append('AAA')
        if starnumber == 2:
            if step[0].strip().endswith('A'):
                start_group.append(step[0].strip())
        dest = step[1].replace('(', '').replace(')', '').replace(' ', '').split(',')
        steps[step[0].strip()] = dest

    return steps, start_group


def find_exit(instructions: list, start_position: str, steps: dict) -> int:
    position = start_position
    count = 0
    while True:
        for order in instructions:
            count += 1
            if order == 'L':
                position = steps[position][0]
            elif order == 'R':
                position = steps[position][1]
            if position.endswith('Z'):
                return count

@measure_time
def stars(starnumber: int, data: list):

    instructions = data[0].strip()
    steps, start_group = create_map(data, starnumber)

    # For star 2 brute force is going to take to long, we need to find when each starting position finds the end (in how
    # many steps) and then find the least common multiple of all of them to find at which step they all meet.

    count_loop = []
    for position in start_group:
        count_loop.append(find_exit(instructions, position, steps))

    if starnumber == 1:
        return count_loop[0]
    elif starnumber == 2:
        return lcm(*count_loop)


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 6, 6, stars, 'test_1.txt', 'test_2.txt')


if __name__ == "__main__":
    main()
