def readlines(input_file: str) -> list:
    """
    Read each line of text file and return a list of strings containing the lines of input file
    :param input_file: filepath to read in string format
    :return: list of strings containing the lines of input file
    """
    # Read each line of text file
    with open(input_file, 'r') as file:
        data = file.read().splitlines()
    return data


def get_neighbors(data: list, x: int, y: int, return_coords: bool = False):
    """ Store neighbors of a given coordinate in a list and return it
    :param data: list of strings containing the lines of input file
    :param x: x coordinate
    :param y: y coordinate
    :param return_coords: if True, return also a dictionary with the coordinates of the neighbors
    :return: list of neighbors
    """
    neighbors = []
    neighbor_coord = {}

    if x > 0:
        neighbors.append(data[y][x - 1])
        neighbor_coord[data[y][x - 1]] = (x - 1, y)
    if x < len(data[y]) - 1:
        neighbors.append(data[y][x + 1])
        neighbor_coord[data[y][x + 1]] = (x + 1, y)
    if y > 0:
        neighbors.append(data[y - 1][x])
        neighbor_coord[data[y - 1][x]] = (x, y - 1)
    if y < len(data) - 1:
        neighbors.append(data[y + 1][x])
        neighbor_coord[data[y + 1][x]] = (x, y + 1)
    if x > 0 and y > 0:
        neighbors.append(data[y - 1][x - 1])
        neighbor_coord[data[y - 1][x - 1]] = (x - 1, y - 1)
    if x < len(data[y]) - 1 and y > 0:
        neighbors.append(data[y - 1][x + 1])
        neighbor_coord[data[y - 1][x + 1]] = (x + 1, y - 1)
    if x > 0 and y < len(data) - 1:
        neighbors.append(data[y + 1][x - 1])
        neighbor_coord[data[y + 1][x - 1]] = (x - 1, y + 1)
    if x < len(data[y]) - 1 and y < len(data) - 1:
        neighbors.append(data[y + 1][x + 1])
        neighbor_coord[data[y + 1][x + 1]] = (x + 1, y + 1)
    if return_coords:
        return neighbors, neighbor_coord
    else:
        return neighbors
