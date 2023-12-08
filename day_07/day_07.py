import os
from typing import Tuple, Any

from adventofcodeutils import measure_time, map_character_count
from aoc_challenge import AocChallenge


def get_cards_type(string, star2=False) -> Tuple[int, Any]:
    hand = map_character_count(string)
    max_value = max(hand.values())
    if max_value == 2:
        if sum(value == 2 for value in hand.values()) == 2:
            if star2 and 'J' in string:
                if hand['J'] == 2:
                    return 6, get_value_hand(string, star2)
                return 5, get_value_hand(string, star2)
            return 3, get_value_hand(string, star2)
        else:
            if star2 and 'J' in string:
                return 4, get_value_hand(string, star2)
            return 2, get_value_hand(string, star2)
    elif max_value == 3:
        if 2 in hand.values():
            if star2 and 'J' in string:
                return 7, get_value_hand(string, star2)
            else:
                return 5, get_value_hand(string, star2)
        if star2 and 'J' in string:
            return 6, get_value_hand(string, star2)
        return 4, get_value_hand(string, star2)
    elif max_value == 4:
        if star2 and 'J' in string:
            return 7, get_value_hand(string, star2)
        return 6, get_value_hand(string, star2)
    elif max_value == 5:
        return 7, get_value_hand(string, star2)
    else:
        if star2 and 'J' in string:
            return 2, get_value_hand(string, star2)
        return 1, get_value_hand(string, star2)


def get_value_hand(hand: str, star2=False) -> int:
    if star2:
        card_values = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
                       '4': 4, '3': 3, '2': 2, 'J': 1}
    else:
        card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
                       '4': 4, '3': 3, '2': 2}
    value = 0
    for i, card in enumerate(reversed(hand)):
        value += card_values[card] * 100 ** i
    return value


def order_hands(games: dict, star2=False):
    def custom_sort(key):
        value = get_cards_type(key, star2)
        return value[0], value[1]

    # Order the keys based on values in the dictionary in reverse order
    ordered_hands = sorted(games.keys(), key=custom_sort)
    return ordered_hands

@measure_time
def stars(starnumber: int, data: list):
    if starnumber == 1:
        star2 = False
    else:
        star2 = True
    game = {}
    for line in data:
        hand, value = line.split(' ')
        game[hand] = value
    game_order = order_hands(game, star2)
    total_value = 0
    for i, hand in enumerate(game_order):
        total_value += int(game[hand]) * (i + 1)
    return total_value


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 6440, 5905, stars)


if __name__ == "__main__":
    main()
