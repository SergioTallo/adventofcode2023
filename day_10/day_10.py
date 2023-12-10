import os
from adventofcodeutils import measure_time, get_neighbors
from aoc_challenge import AocChallenge


def find_starting_point(data: list):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                return j, i


def check_pipe_connection(neighbors: tuple, old_entry_point: tuple, position: tuple, pipe: str) -> tuple:
    pipes = {'|': {'L': [(0, 1)], 'F': [(0, -1)], 'J': [(0, 1)], '7': [(0, -1)], '|': [(0, 1), (0, -1)],
                   'S': [(0, 1), (0, -1)]},
             '-': {'L': [(-1, 0)], 'F': [(-1, 0)], 'J': [(1, 0)], '7': [(1, 0)], '-': [(1, 0), (-1, 0)],
                   'S': [(1, 0), (-1, 0)]},
             'F': {'L': [(0, 1)], 'J': [(0, 1), (1, 0)], '7': [(1, 0)], '|': [(0, 1)], '-': [(1, 0)],
                   'S': [(0, 1), (1, 0)]},
             'L': {'F': [(0, -1)], 'J': [(1, 0)], '7': [(1, 0), (0, -1)], '|': [(0, - 1)], '-': [(1, 0)],
                   'S': [(1, 0), (0, -1)]},
             '7': {'L': [(-1, 0), (0, 1)], 'J': [(0, 1)], 'F': [(-1, 0)], '|': [(0, 1)], '-': [(-1, 0)],
                   'S': [(0, 1), (-1, 0)]},
             'J': {'L': [(-1, 0)], 'F': [(-1, 0), (0, -1)], '7': [(0, -1)], '|': [(0, -1)], '-': [(-1, 0)],
                   'S': [(0, -1), (-1, 0)]},
             'S': {'L': [(0, 1), (-1, 0)], 'J': [(0, 1), (1, 0)], '7': [(1, 0), (0, -1)], '|': [(0, 1), (0, 11)],
                   '-': [(1, 0), (-1, 0)], 'F': [(0, -1), (-1, 0)]}
             }

    for i, neighbor in enumerate(neighbors[0]):
        if neighbor in pipes[pipe]:
            if neighbors[1][i] != old_entry_point:
                for pos_positions in pipes[pipe][neighbor]:
                    pos = (position[0] + pos_positions[0], position[1] + pos_positions[1])
                    if pos == neighbors[1][i]:
                        return neighbor, neighbors[1][i]


@measure_time
def stars(starnumber: int, data: list):
    loop = []
    position = find_starting_point(data)
    pipe = 'S'
    old_entry_point = position
    steps = 0
    while True:
        old_position = position
        neighbors = get_neighbors(data, position[0], position[1], True, False, False)
        pipe, position = check_pipe_connection(neighbors, old_entry_point, position, pipe)
        old_entry_point = old_position
        steps += 1
        loop.append(position)
        if pipe == 'S':
            if starnumber == 1:
                return int(steps / 2)
            break
    if starnumber == 2:
        inside_loop = 0
        for i, line in enumerate(data):
            loop_knots = 0
            for j, tile in enumerate(line):
                if tile in ['|', 'J', 'L', 'S'] and (j, i) in loop:
                    loop_knots += 1
                elif (j, i) not in loop and loop_knots % 2 != 0:
                    inside_loop += 1
        return inside_loop


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 8, 10, stars, test_file1='test1.txt', test_file2='test2.txt')


if __name__ == "__main__":
    main()
