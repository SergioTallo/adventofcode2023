import os
from adventofcodeutils import measure_time, transform_to_list
from aoc_challenge import AocChallenge


def inside_map(y: int, x: int, data: list) -> bool:
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[0]):
        return False
    else:
        return True


def next_position(y: int, x: int, direction: tuple, positions: list, data: list) -> list:
    if data[y][x] == '.':
        if inside_map(y + direction[0], x + direction[1], data):
            positions.append(((y + direction[0], x + direction[1]), direction))
    if data[y][x] == '-':
        if direction == (0, -1) or direction == (0, 1):
            if inside_map(y + direction[0], x + direction[1], data):
                positions.append(((y + direction[0], x + direction[1]), direction))
        else:
            if inside_map(y, x - 1, data):
                positions.append(((y, x - 1), (0, -1)))
            if inside_map(y, x + 1, data):
                positions.append(((y, x + 1), (0, 1)))
    if data[y][x] == '|':
        if direction == (-1, 0) or direction == (1, 0):
            if inside_map(y + direction[0], x + direction[1], data):
                positions.append(((y + direction[0], x + direction[1]), direction))
        else:
            if inside_map(y - 1, x, data):
                positions.append(((y - 1, x), (-1, 0)))
            if inside_map(y + 1, x, data):
                positions.append(((y + 1, x), (1, 0)))
    if data[y][x] == '/':
        new_direction = (direction[1] * -1, direction[0] * -1)
        if inside_map(y + new_direction[0], x + new_direction[1], data):
            positions.append(((y + new_direction[0], x + new_direction[1]), new_direction))
    if data[y][x] == '\\':
        new_direction = (direction[1], direction[0])
        if inside_map(y + new_direction[0], x + new_direction[1], data):
            positions.append(((y + new_direction[0], x + new_direction[1]), new_direction))

    return positions


def light_next_position(data: list, y: int, x: int, direction: tuple, positions: list, visited_positions: list,
                        energised_positions: list) -> tuple:
    if ((y, x), direction) in visited_positions:
        return positions, visited_positions, energised_positions
    else:
        positions = next_position(y, x, direction, positions, data)
        visited_positions.append(((y, x), direction))
        if (y, x) not in energised_positions:
            energised_positions.append((y, x))

    return positions, visited_positions, energised_positions


def append_position(data: list, positions: list) -> int:
    visited_positions = []
    energised_positions = []
    while len(positions) > 0:
        pos_dir = positions.pop()
        positions, visited_positions, energised_positions = light_next_position(data, pos_dir[0][0], pos_dir[0][1],
                                                                                pos_dir[1],
                                                                                positions, visited_positions,
                                                                                energised_positions)
    return len(energised_positions)


def append_position2(data: list, positions: list, starts: dict) -> tuple:
    visited_positions = []
    energised_positions = []
    while len(positions) > 0:
        pos_dir = positions.pop()
        if (pos_dir[0], pos_dir[1]) in starts:
            for pos in starts[(pos_dir[0], pos_dir[1])]:
                if pos not in positions:
                    positions.append((pos[0], pos[1]))
                if pos[0] not in energised_positions:
                    energised_positions.append(pos[0])
        positions, visited_positions, energised_positions = light_next_position(data, pos_dir[0][0], pos_dir[0][1],
                                                                                pos_dir[1],
                                                                                positions, visited_positions,
                                                                                energised_positions)

    return visited_positions, energised_positions


@measure_time
def stars(starnumber: int, data: list):
    data = transform_to_list(data)

    if starnumber == 1:
        energised_positions_count = append_position(data, [((0, 0), (0, 1))])
        return energised_positions_count
    if starnumber == 2:
        starts = {}
        max_count = 0
        for j in range(len(data[0])):
            starts[((0, j), (1, 0))] = append_position2(data, [((0, j), (1, 0))], starts)
            count = len(starts[((0, j), (1, 0))][1])
            if count > max_count:
                max_count = count

            starts[((len(data) - 1, j), (-1, 0))] = append_position2(data, [((len(data) - 1, j), (-1, 0))], starts)
            count = len(starts[((len(data) - 1, j), (-1, 0))][1])
            if count > max_count:
                max_count = count

        for i in range(len(data)):
            starts[((i, 0), (0, 1))] = append_position2(data, [((i, 1), (0, 1))], starts)
            count = len(starts[((i, 0), (0, 1))][1])
            if count > max_count:
                max_count = count

            starts[((i, len(data[i]) - 1), (0, -1))] = append_position2(data, [((i, len(data[i]) - 1), (0, -1))],
                                                                        starts)
            count = len(starts[((i, len(data[i]) - 1), (0, -1))][1])
            if count > max_count:
                max_count = count

        return max_count


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 46, 51, stars)


if __name__ == "__main__":
    main()
