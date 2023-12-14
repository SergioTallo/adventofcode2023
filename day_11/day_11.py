import os
from adventofcodeutils import measure_time, transform_to_list
from aoc_challenge import AocChallenge


def shortest_path(galaxy: tuple, galaxy2: tuple, expanded_universe: tuple, expansion: int) -> int:
    x = abs(galaxy[0] - galaxy2[0])
    y = abs(galaxy[1] - galaxy2[1])
    expand = 0
    for i in expanded_universe[0]:
        if i in range(galaxy[0], galaxy2[0]) or i in range(galaxy2[0], galaxy[0]):
            expand += expansion
    for i in expanded_universe[1]:
        if i in range(galaxy[1], galaxy2[1]) or i in range(galaxy2[1], galaxy[1]):
            expand += expansion
    return x + y + expand


def find_galaxies(universe: list) -> dict:
    galaxies = {}
    count = 1
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] == '#':
                galaxies[str(count)] = (i, j)
                count += 1
    return galaxies


def expand_universe(universe: list) -> tuple:
    list_expand_y = []
    list_expand_x = []
    for i in range(len(universe)):
        if '#' not in universe[i]:
            list_expand_y.append(i)
    for i in range(len(universe[0])):
        if '#' not in [row[i] for row in universe]:
            list_expand_x.append(i)
    return list_expand_y, list_expand_x


@measure_time
def stars(starnumber: int, data: list):
    universe = transform_to_list(data)
    expanded_universe = expand_universe(universe)
    galaxies = find_galaxies(universe)
    total_1 = 0
    total_2 = 0
    for i, galaxy1 in enumerate(galaxies):
        for j, galaxy2 in enumerate(galaxies):
            if i < j:
                if starnumber == 1:
                    total_1 += shortest_path(galaxies[galaxy1], galaxies[galaxy2], expanded_universe, 1)
                if starnumber == 2:
                    total_2 += shortest_path(galaxies[galaxy1], galaxies[galaxy2], expanded_universe, 999999)
    if starnumber == 1:
        return total_1
    if starnumber == 2:
        return total_2


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 374, 82000210, stars)


if __name__ == "__main__":
    main()
