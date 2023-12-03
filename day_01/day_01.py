from adventofcodeutils import readlines

data = readlines('input.txt')

# First star

sum_of_values = 0
for line in data:
    for char in line:
        if char.isdecimal():
            for char2 in reversed(line):
                if char2.isdecimal():
                    sum_of_values += int((f"{char}{char2}"))
                    break
            break

print(f"Sum of values (first star): {sum_of_values}")

# Second star

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

sum_of_values = 0

for line in data:
    line = line.strip()

    line_n = words_to_numbers(line)
    line_r = words_to_numbers(line, reversed=True)

    for char in line_n:
        if char.isdecimal():
            for char2 in reversed(line_r):
                if char2.isdecimal():
                    sum_of_values += int((f"{char}{char2}"))
                    break
            break

print(f"Sum of values (second star): {sum_of_values}")