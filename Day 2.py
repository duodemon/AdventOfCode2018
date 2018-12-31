from utility import convert_input_to_string


def part1(puzzle_input):
    """
    Goes through each line in the input and finds the ID with letters that appear exactly 2 and 3 times, then multiplies
    them together.

    :param puzzle_input:
    :return: Numbers of IDs with letters appearing exactly twice
    """

    puzzle_input_arr = puzzle_input.split('\n')
    number_of_ids_with_letter_appearing_twice = 0
    number_of_ids_with_letter_appearing_thrice = 0
    for _id in puzzle_input_arr:
        number_of_appearances_letter = {}  # letter: number of appearances in the word
        for letter in _id:
            if letter not in number_of_appearances_letter:
                number_of_appearances_letter[letter] = 1
            else:
                number_of_appearances_letter[letter] += 1
        if 2 in number_of_appearances_letter.values():
            number_of_ids_with_letter_appearing_twice += 1
        if 3 in number_of_appearances_letter.values():
            number_of_ids_with_letter_appearing_thrice += 1
    return number_of_ids_with_letter_appearing_twice * number_of_ids_with_letter_appearing_thrice


def part2(puzzle_input):
    """
    In the puzzle input, there is only one pair of IDs that differ by exactly one letter. This function finds it and
    returns the letters in common.

    Goes through every letter in every ID and replaces it with '.' and stores the ID in a set. If the pattern already
    exists, then that is the duplicate. Return all the other letters.

    :param puzzle_input:
    :return: Numbers of IDs with letters appearing exactly twice
    """

    patterns = set()
    puzzle_input_arr = puzzle_input.strip().split('\n')
    for _id in puzzle_input_arr:
        for (index, letter) in enumerate(_id):
            pattern = _id[:index] + '.' + _id[index + 1:]
            if pattern in patterns:
                return pattern.replace('.', '')
            patterns.add(pattern)


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 2.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))