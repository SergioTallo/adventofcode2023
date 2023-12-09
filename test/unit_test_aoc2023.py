import unittest
from adventofcodeutils import readlines, get_numbers_in_string, get_neighbors, map_character_count
from day_01.day_01 import words_to_numbers
from day_06.day_06 import quadratic_equation_solve
from day_07.day_07 import get_cards_type, get_value_hand, order_hands
from day_09.day_09 import generate_sequence, extrapolated_value

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
        self.assertEqual(map_character_count('AA3KE'), {'A': 2, '3': 1, 'K': 1, 'E': 1})
        self.assertEqual(map_character_count('AA3KK'), {'A': 2, '3': 1, 'K': 2})

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

    def test_7(self):
        self.assertEqual(get_value_hand('32T3K'), 302100313)
        self.assertEqual(get_value_hand('T55J5'), 1005051105)
        self.assertEqual(get_value_hand('KK677'), 1313060707)
        self.assertEqual(get_value_hand('KTJJT'), 1310111110)
        self.assertEqual(get_value_hand('QQQJA'), 1212121114)
        self.assertEqual(get_cards_type('32T3K'), (2, 302100313))
        self.assertEqual(get_cards_type('T55J5'), (4, 1005051105))
        self.assertEqual(get_cards_type('KK677'), (3, 1313060707))
        self.assertEqual(get_cards_type('KTJJT'), (3, 1310111110))
        self.assertEqual(get_cards_type('QQQJA'), (4, 1212121114))
        self.assertEqual(order_hands({'32T3K': '765', 'T55J5': '684', 'KK677': '28', 'KTJJT': '220', 'QQQJA': '483'}),
                         ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA'])
        self.assertEqual(
            order_hands({'32T3K': '765', 'T55J5': '684', 'KK677': '28', 'KTJJT': '220', 'QQQJA': '483'}, True),
            ['32T3K', 'KK677', 'T55J5', 'QQQJA', 'KTJJT'])

    def test_9(self):
        self.assertEqual(generate_sequence([0, 3, 6, 9, 12, 15]), [3, 3, 3, 3, 3])
        self.assertEqual(generate_sequence([1, 3, 6, 10, 15, 21]), [2, 3, 4, 5, 6])
        self.assertEqual(generate_sequence([10, 13, 16, 21, 30, 45]), [3, 3, 5, 9, 15])
        self.assertEqual(generate_sequence([-24, -207, -663, -1671, -3708, -7541, -14344]), [-183, -456, -1008, -2037, -3833, -6803])
        self.assertEqual(extrapolated_value('0 3 6 9 12 15'), 18)
        self.assertEqual(extrapolated_value('1 3 6 10 15 21'), 28)
        self.assertEqual(extrapolated_value('10 13 16 21 30 45'), 68)