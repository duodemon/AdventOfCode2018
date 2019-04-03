from utility import convert_input_to_string
import re

def part1_2(puzzle_input):
    """
    The text file contains an initial state and all the rules. After each cycle, the string gets updated by the rules.
    The left hand side is a pattern. For each character in the string, if its left two characters plus the character itself
    plus its right two characters match the pattern, that character becomes the character on the right hand side of the
    rule.

    Part 1 returns the sum of all the indices where its character equals '#' after 20 cycles.

    Part 2 returns the sum of all the indices where its character equals '#' after 50 billion cycles.

    :param puzzle_input:
    :return:
    """
    [initial_state_string, configurations] = puzzle_input.split('\n\n')
    initial_state = re.sub('initial state: ', '', initial_state_string)
    rules_arr = configurations.split('\n')
    rules = [re.split(' => ', line) for line in rules_arr]
    rules = {t[0]: t[1] for t in rules}
    current_state = '..........' + initial_state + '...............................................................................................................................................'
    for i in range(100):  # After 100th cycle, the only change is that there is a '#' that shifts right
        next_generation_string = ""
        for index, pot in enumerate(current_state):
            if index == 0:
                temp_string = '..' + current_state[:3]
            elif index == 1:
                temp_string = '.' + current_state[:4]
            elif index == len(current_state) - 2:
                temp_string = current_state[-4:] + '.'
            elif index == len(current_state) - 1:
                temp_string = current_state[-3:] + '..'
            else:
                temp_string = current_state[index-2:index+3]
            if temp_string in rules:
                next_generation_string += rules[temp_string]
            else:
                next_generation_string += pot
        current_state = next_generation_string

        # For part 1
        part1_sum = 0
        if i == 19:
            for index, pot in enumerate(current_state):
                if pot == '#':
                    part1_sum += index - 10
            print(part1_sum)

    # Part 2
    part2_sum = 0
    for index, pot in enumerate(current_state):
        if pot == '#':
            part2_sum += index - 10 + 50000000000 - 100
    print(part2_sum)

if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 12.txt")
    part1_2(puzzle_input)