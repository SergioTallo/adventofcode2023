import functools
import os
import requests
import time
import re


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


def transform_to_list(data: list) -> list:
    """
    Transform a list of strings into a list of lists of characters
    :param data:
    :return:
    """
    return [list(line) for line in data]


def get_neighbors(data: list, x: int, y: int, return_coords: bool = False, check_corners: bool = True, dictionary: bool = True):
    """ Store neighbors of a given coordinate in a list and return it
    :param dictionary: return the coordinates of the neighbors in a dictionary
    :param data: list of strings containing the lines of input file
    :param x: x coordinate
    :param y: y coordinate
    :param return_coords: if True, return also a dictionary with the coordinates of the neighbors
    :param check_corners: if True, check also the corners
    :return: list of neighbors
    """
    neighbors = []
    neighbor_coord = []
    neighbor_coord_dict = {}

    if x > 0:
        neighbors.append(data[y][x - 1])
        neighbor_coord_dict[data[y][x - 1]] = (x - 1, y)
        neighbor_coord.append((x - 1, y))
    if x < len(data[y]) - 1:
        neighbors.append(data[y][x + 1])
        neighbor_coord_dict[data[y][x + 1]] = (x + 1, y)
        neighbor_coord.append((x + 1, y))
    if y > 0:
        neighbors.append(data[y - 1][x])
        neighbor_coord_dict[data[y - 1][x]] = (x, y - 1)
        neighbor_coord.append((x, y - 1))
    if y < len(data) - 1:
        neighbors.append(data[y + 1][x])
        neighbor_coord_dict[data[y + 1][x]] = (x, y + 1)
        neighbor_coord.append((x, y + 1))
    if check_corners and x > 0 and y > 0:
        neighbors.append(data[y - 1][x - 1])
        neighbor_coord_dict[data[y - 1][x - 1]] = (x - 1, y - 1)
        neighbor_coord.append((x - 1, y - 1))
    if check_corners and x < len(data[y]) - 1 and y > 0:
        neighbors.append(data[y - 1][x + 1])
        neighbor_coord_dict[data[y - 1][x + 1]] = (x + 1, y - 1)
        neighbor_coord.append((x + 1, y - 1))
    if check_corners and x > 0 and y < len(data) - 1:
        neighbors.append(data[y + 1][x - 1])
        neighbor_coord_dict[data[y + 1][x - 1]] = (x - 1, y + 1)
        neighbor_coord.append((x - 1, y + 1))
    if check_corners and x < len(data[y]) - 1 and y < len(data) - 1:
        neighbors.append(data[y + 1][x + 1])
        neighbor_coord_dict[data[y + 1][x + 1]] = (x + 1, y + 1)
        neighbor_coord.append((x + 1, y + 1))

    if return_coords:
        if dictionary:
            return neighbors, neighbor_coord_dict
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


def get_numbers_in_string(string: str) -> list:
    """
    Get all numbers in a string and return them in a list
    :param string: string to search for numbers
    :return: list of numbers
    """
    pattern = r'-?\d+'
    numbers = re.findall(pattern, string)
    return [int(num) for num in numbers]


def map_character_count(string) -> dict:
    """
    Map the number of occurrences of each character in a string
    :param string: string to map
    :return: dictionary with the number of occurrences of each character
    """
    character_counts = {}

    for character in string:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    return character_counts
