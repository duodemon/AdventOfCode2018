from utility import convert_input_to_string


def part1(puzzle_input):
    """ sums each line in a text file of frenquencies (signed ints).

    :param puzzle_input: the text file to string
    :return: the sum of all the frequencies
    """
    puzzle_input_arr = puzzle_input.split('\n')
    aggregate_frequency = 0
    for frequency in puzzle_input_arr:
        aggregate_frequency += int(frequency)
    return aggregate_frequency


def part2(puzzle_input):
    """ sums each line in a text file of frenquencies (signed ints)
    and finds the first resulting frequency that appears twice. Wraps around to the start
    of the file and repeats until found. Using a set instead of list for visited_frequencies
    decreased runtime by over 100% due to hashing.

    :param puzzle_input: the text file to string
    :return: the first resulting frequency that appears twice
    """
    puzzle_input_arr = puzzle_input.split('\n')
    aggregate_frequency = 0
    visited_frequencies = {0}
    duplicate_not_found = True
    while duplicate_not_found:
        for frequency in puzzle_input_arr:
            aggregate_frequency += int(frequency)
            if aggregate_frequency not in visited_frequencies:
                visited_frequencies.add(aggregate_frequency)
            else:
                duplicate_not_found = False
                break
    return aggregate_frequency


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 1.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))