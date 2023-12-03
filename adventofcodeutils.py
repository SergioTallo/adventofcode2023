import os
import requests


def download_input(year: int, day: int, cookie_file_path: str):
    """
    Download input file from Advent of Code website and save it in the current directory
    :param year: year of the challenge
    :param day: day of the challenge
    :param cookie_file_path: filepath to read in string format
    :return: None
    """
    if not os.path.exists(f'input_day{day}.txt'):
        session_cookie = ''
        if os.path.exists(cookie_file_path):
            with open(cookie_file_path, 'r') as file:
                session_cookie = file.read().strip()
        else:
            print("Session cookie file not found.")

        # Replace 'YOUR_SESSION_COOKIE' with your session cookie from Advent of Code website
        cookies = {'session': session_cookie}

        url = f'https://adventofcode.com/{year}/day/{day}/input'
        response = requests.get(url, cookies=cookies)

        if response.status_code == 200:
            with open(f'input_day{day}.txt', 'w') as file:
                file.write(response.text)
        else:
            print(f"Failed to download input for day {day}. Status code: {response.status_code}")


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


class aoc_challenge():
    """
    Advent of Code challenge class

    :param day: day of the challenge
    :param year: year of the challenge
    :param cookie_file_path: filepath to read personal session cookie in string format
    :method test: test the challenge
    :method challenge: run the challenge
    """
    def __init__(self, day: int, year: int, cookie_file_path: str):
        self.day = day
        self.year = year
        self.cookie_file_path = cookie_file_path
        download_input(self.year, self.day, self.cookie_file_path)

    def test(self, func_1, func_2, value_1, value_2):
        print("############## Tests ##############\n")
        print(f"Testing start 1, day {self.day}...")
        assert func_1 == value_1, f"Star one failed, should be {value_1} but is {func_1}"
        print("Test 1 passed")
        print(f"Testing start 2, day {self.day}...")
        assert func_2 == value_2, f"Star two failed, should be {value_2} but is {func_2}"
        print("Test 2 passed\n")

    def challenge(self, func_1, func_2):
        print("############## Challenge ##############\n")
        print(f"Score 1: {func_1}")
        print(f"Score 2: {func_2}")
