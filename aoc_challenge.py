import os
from adventofcodeutils import download_input, readlines


class AocChallenge:
    """
    Advent of Code challenge class

    :param day: day of the challenge
    :param year: year of the challenge
    :method test: test the challenge
    :method challenge: run the challenge
    """

    def __init__(self, day: int, year: int, value_1: int, value_2: int, function, test_file1='test_1.txt',
                 test_file2='test_1.txt'):
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