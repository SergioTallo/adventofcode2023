import os
from adventofcodeutils import readlines, aoc_challenge


def words_to_numbers(text, reversed=False):
    words_to_nums = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    if reversed:
        ordered_words = sorted(words_to_nums, key=lambda x: text[::-1].find(x[::-1]))

        # text[::-1].find(x[::-1]) is the same as text.find(x) but reversing the text and the word to find

    else:
        ordered_words = sorted(words_to_nums, key=lambda x: text.find(x))

    for word in ordered_words:
        text = text.replace(word, words_to_nums[word])

    return text

def stars(starnumber, data):
    sum_of_values = 0

    if starnumber == 1:
        for line in data:
            for char in line:
                if char.isdecimal():
                    for char2 in reversed(line):
                        if char2.isdecimal():
                            sum_of_values += int(f"{char}{char2}")
                            break
                    break
        return sum_of_values

    elif starnumber == 2:
        for line in data:
            line = line.strip()

            line_n = words_to_numbers(line)
            line_r = words_to_numbers(line, reversed=True)

            for char in line_n:
                if char.isdecimal():
                    for char2 in reversed(line_r):
                        if char2.isdecimal():
                            sum_of_values += int(f"{char}{char2}")
                            break
                    break
        return sum_of_values

def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    aoc_challenge(day, 2023, 142, 281, stars, 'test_1.txt', 'test_2.txt')


if __name__ == "__main__":
    main()