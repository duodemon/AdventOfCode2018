from utility import convert_input_to_string


def part1(puzzle_input):
    puzzle_input_arr = puzzle_input.split('\n')
    number_of_ids_with_letter_appearing_twice = 0
    number_of_ids_with_letter_appearing_thrice = 0
    for _id in puzzle_input_arr:
        number_of_appearances_letter = {}
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
    puzzle_input_arr = puzzle_input.split('\n')
    for (index, _id) in enumerate(puzzle_input_arr):
        puzzle_input_arr_without_current_id = puzzle_input_arr[:index] + puzzle_input_arr[index + 1:]
        for _id_to_compare in puzzle_input_arr_without_current_id:
            number_of_different_letters = 0
            for letter_index in range(len(_id_to_compare)):
                if _id[letter_index] != _id_to_compare[letter_index]:
                    number_of_different_letters += 1
                    if number_of_different_letters > 1:
                        break
            if number_of_different_letters == 1 :
                for letter_index in range(len(_id_to_compare)):
                    if _id[letter_index] != _id_to_compare[letter_index]:
                        return _id[:letter_index] + _id[letter_index+1:]


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 2.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))