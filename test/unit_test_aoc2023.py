import unittest
from adventofcodeutils import readlines, get_numbers_in_string, get_neighbors
from day_01.day_01 import words_to_numbers
from day_06.day_06 import quadratic_equation_solve


class TestAoC2023(unittest.TestCase):
    def test_0(self):
        self.assertEqual(readlines('test.txt'), ['two1nine', 'eightwothree', 'abcone2threexyz', 'nineeightseven2'])
        self.assertEqual(get_numbers_in_string('Distance:  9  40  200'), [9, 40, 200])
        self.assertEqual(get_numbers_in_string('Distance:9,40,200'), [9, 40, 200])
        self.assertEqual(get_numbers_in_string('Distance:9ezhhd40adkjhd200sjkdffsh'), [9, 40, 200])
        self.assertEqual(get_neighbors(['467..114..', '...*......', '..35..633.', '......#...'], 0, 0, False),
                         ['6', '.', '.'])
        self.assertEqual(get_neighbors(['467..114..', '...*......', '..35..633.', '......#...'], 2, 2, False),
                            ['.', '5', '.', '.', '.', '*', '.', '.'])
        self.assertEqual(get_neighbors(['467..114..', '...*......', '..35..633.', '......#...'], 0, 0, True),
                         (['6', '.', '.'], {'.': (1, 1), '6': (1, 0)}))
        self.assertEqual(get_neighbors(['467..114..', '...*......', '..35..633.', '......#...'], 2, 2, True),
                         (['.', '5', '.', '.', '.', '*', '.', '.'], {'*': (3, 1), '.': (3, 3), '5': (3, 2)}))


    def test_1(self):
        self.assertEqual(words_to_numbers('two1nine', False), '219')
        self.assertEqual(words_to_numbers('eightwothree', False), '8wo3')
        self.assertEqual(words_to_numbers('abcone2threexyz', False), 'abc123xyz')
        self.assertEqual(words_to_numbers('nineeightseven2', False), '9872')
        self.assertEqual(words_to_numbers('zoneight234', False), 'z1ight234')
        self.assertEqual(words_to_numbers('pqrstsixteen', False), 'pqrst6teen')
        self.assertEqual(words_to_numbers('two1nine', True), '219')
        self.assertEqual(words_to_numbers('eightwothree', True), 'eigh23')
        self.assertEqual(words_to_numbers('abcone2threexyz', True), 'abc123xyz')
        self.assertEqual(words_to_numbers('nineeightseven2', True), '9872')
        self.assertEqual(words_to_numbers('zoneight234', True), 'zon8234')
        self.assertEqual(words_to_numbers('pqrstsixteen', True), 'pqrst6teen')

    def test_6(self):
        self.assertEqual(quadratic_equation_solve(7, 9), (2, 5))
        self.assertEqual(quadratic_equation_solve(15, 40), (4, 11))
        self.assertEqual(quadratic_equation_solve(30, 200), (11, 19))
