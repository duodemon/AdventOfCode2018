from utility import convert_input_to_string
import re


def part1(polymer):
    """
    The text input file is a long string. That string is a chemical polymer. Part 1 parses the input and removes all
    units which are adjacent to the same unit but opposite polarity (upper/lowercase letters adjacent to each other) and
    keeps on repeating until there are no more reactive units. Finds the length of the remaining polymer.

    :param polymer: a string of letters
    :return: the number of units remaining
    """
    reaction_map = {"aA", "bB", "cC", "dD", "eE", "fF", "gG", "hH", "iI", "jJ", "kK", "lL", "mM", "nN", "oO", "pP",
                    "qQ", "rR", "sS", "tT", "uU", "vV", "wW", "xX", "yY", "zZ", "Aa", "Bb", "Cc", "Dd", "Ee", "Ff",
                    "Gg", "Hh", "Ii", "Jj", "Kk", "Ll", "Mm", "Nn", "Oo", "Pp", "Qq", "Rr", "Ss", "Tt", "Uu", "Vv",
                    "Ww", "Xx", "Yy", "Zz"}
    while True:
        initial_length = len(polymer)
        polymer = re.sub("|".join(reaction_map), "", polymer)
        if len(polymer) == initial_length:
            return len(polymer)


def part2(polymer):
    """
    The text input file is a long string. That string is a chemical polymer. Part 2 parses the input and removes all
    units of a single letter and get its resulting length. Finds the shortest polymer after removing all units of one type.

    :param polymer: a string of letters
    :return: the length of the shortest polymer after removing all units of one type
    """
    unit_to_final_length = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                            'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                            'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for unit in unit_to_final_length:
        unit_to_final_length[unit] = part1(re.sub(unit + '|' + unit.lower(), '', polymer))
    return min(unit_to_final_length)


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 5.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))