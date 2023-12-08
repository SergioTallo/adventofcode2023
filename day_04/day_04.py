import os
from adventofcodeutils import AocChallenge, measure_time
import re


@measure_time
def stars(starnumber: int, data: list):
    pile_scratchcards = [1 for _ in range(len(data))]
    score = 0
    for card_number, card in enumerate(data):
        card = card.split(':')[1].strip()

        # regex to find numbers and store the on list
        pattern = r'(\d+)'
        winning_numbers = re.findall(pattern, card.split('|')[0].strip())
        owning_numbers = re.findall(pattern, card.split('|')[1].strip())

        count = len(set(winning_numbers) & set(owning_numbers))

        if starnumber == 1:
            if count > 0:
                score += 2 ** (count - 1)
        elif starnumber == 2:
            for i in range(count):
                pile_scratchcards[card_number + i + 1] += 1 * pile_scratchcards[card_number]

    if starnumber == 1:
        return score
    elif starnumber == 2:
        return sum(pile_scratchcards)


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    AocChallenge(day, 2023, 13, 30, stars)


if __name__ == "__main__":
    main()
