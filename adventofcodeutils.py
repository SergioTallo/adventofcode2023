import functools
import os
import requests
import time


def download_input(year: int, day: int, cookie_file_path: str):
    """
    Download input file from Advent of Code website and save it in the current directory
    :param year: year of the challenge
    :param day: day of the challenge
    :param cookie_file_path: filepath to read in string format
    :return: None
    """
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


def measure_time(func):
    """
    Measure the execution time of a function
    :param func: Function to measure
    :return: wrapper function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function
        :param args: arguments
        :param kwargs: keyword arguments
        :return: result of the function
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for '{func.__name__}': {execution_time} seconds")
        return result

    return wrapper


class aoc_challenge:
    """
    Advent of Code challenge class

    :param day: day of the challenge
    :param year: year of the challenge
    :method test: test the challenge
    :method challenge: run the challenge
    """

    def __init__(self, day: int, year: int, value_1: int, value_2: int, function, test_file1='test.txt',
                 test_file2='test.txt'):
        self.day = day
        self.year = year
        self.function = function
        self.test_file1 = test_file1
        self.test_file2 = test_file2
        self.value_1 = value_1
        self.value_2 = value_2

        try:
            if not os.path.exists(f'input_day{day}.txt'):
                current_directory = os.path.abspath(os.path.dirname(__file__))
                self.cookie_file_path = os.path.join(current_directory, 'session_cookie.txt')
                download_input(self.year, self.day, self.cookie_file_path)
            self.data_input = readlines(f'input_day{self.day}.txt')
            self.data_test1 = readlines(self.test_file1)
            self.data_test2 = readlines(self.test_file2)
        except FileNotFoundError:
            print(f"File not found.")
            self.data_input = None
            self.data_test1 = None
            self.data_test2 = None

        self.test()
        self.challenge()

    def test(self):
        """
        Test the challenge
        :return: None
        """
        print("\n############## Tests ##############\n")
        print(f"Testing star one, day {self.day}...")
        assert self.function(1, self.data_test1) == self.value_1, \
            f"Star one failed, should be {self.value_1} but is {self.function(1, self.test_file1)}"
        print("Test 1 passed")
        print(f"Testing star two, day {self.day}...")
        assert self.function(2, self.data_test2) == self.value_2, \
            f"Star two failed, should be {self.value_2} but is {self.function(2, self.test_file2)}"
        print("Test 2 passed")

    def challenge(self):
        """
        Run the challenge
        :return: None
        """
        print("\n############## Challenge ##############\n")
        print(f"Score 1: {self.function(1, self.data_input)}")
        print(f"Score 2: {self.function(2, self.data_input)}")
