from utility import convert_input_to_string
from collections import defaultdict
import re
import copy


class Cell:
    def __init__(self):
        self.x_coord = 1
        self.y_coord = 1
        self.rack_id = 0


def part1(puzzle_input):
    """
    The puzzle input is an integer used to find the power level of a cell of a fuel grid (2x2 square) (see function below).
    Part 1 finds the coordinates of the top left cell of a 3x3 square with the largest total power.
    :param puzzle_input:
    :return: the coordinates of the top left cell of the 3x3 square with maximum power
    """
    coords_to_power_level = {}
    power_sums_of_squares = defaultdict(int)
    max_size = 300
    size_square = 3
    for x_coord in range(max_size):
        for y_coord in range(max_size):
            if x_coord + 1 <= max_size - 2 and y_coord + 1 <= max_size - 2:
                for x in range(size_square):
                    for y in range(size_square):
                        if (x_coord + 1 + x, y_coord + 1 + y) not in coords_to_power_level:
                            coords_to_power_level[(x_coord + 1 + x, y_coord + 1 + y)] = find_power_level(int(puzzle_input), x_coord + 1 + x, y_coord + 1 + y)
                        power_sums_of_squares[(x_coord + 1, y_coord + 1)] += coords_to_power_level[x_coord + 1 + x, y_coord + 1 + y]
    return max(power_sums_of_squares, key=power_sums_of_squares.get)


def part2(puzzle_input):
    """
    The puzzle input is an integer used to find the power level of a cell of a fuel grid (2x2 square) (see function below).
    Part 2 finds the top left cell of a size*size square with the maximum total power.

    Note on runtimes, brute forcing has a runtime of O(n^5), where n is the max size of the fuel grid. Therefore, I used
    a summed area table to memoize and reduce the runtime to O(n^3).
    :param puzzle_input:
    :return: the coordinates of the top left cell of the size*size square with maximum power along with the size of square
    """
    coords_to_summed_area_table = {}
    max_size = 300
    for x_coord in range(max_size):
        for y_coord in range(max_size):
            power_level = find_power_level(int(puzzle_input), y_coord + 1, x_coord + 1)
            if x_coord + 1 == 1 and y_coord + 1 == 1:
                coords_to_summed_area_table[(x_coord + 1, y_coord + 1)] = power_level
            elif y_coord + 1 == 1:
                coords_to_summed_area_table[x_coord + 1, y_coord + 1] = power_level + coords_to_summed_area_table[x_coord, y_coord + 1]
            elif x_coord + 1 == 1:
                coords_to_summed_area_table[x_coord + 1, y_coord + 1] = power_level + coords_to_summed_area_table[x_coord + 1, y_coord]
            else:
                coords_to_summed_area_table[x_coord + 1, y_coord + 1] = power_level + coords_to_summed_area_table[x_coord + 1, y_coord] \
                                                                        + coords_to_summed_area_table[x_coord, y_coord + 1] - coords_to_summed_area_table[x_coord, y_coord]
    power_sums_of_squares_and_sizes = defaultdict(int)
    for x_coord in range(max_size):
        for y_coord in range(max_size):
            for size in range(max_size):
                if x_coord + 1 <= max_size - size and y_coord + 1 <= max_size - size:
                    if size + 1 == 1:
                        power_sums_of_squares_and_sizes[x_coord + 1, y_coord + 1, size + 1] = coords_to_summed_area_table[x_coord + 1 , y_coord + 1]
                    else:
                        power_sums_of_squares_and_sizes[x_coord + 1, y_coord + 1, size + 1] = coords_to_summed_area_table[x_coord + 1 + size, y_coord + 1 + size] - coords_to_summed_area_table[x_coord + 1, y_coord + 1 + size] \
                                                                                            - coords_to_summed_area_table[x_coord + 1 + size, y_coord + 1] + coords_to_summed_area_table[x_coord + 1, y_coord + 1]
    return max(power_sums_of_squares_and_sizes, key=power_sums_of_squares_and_sizes.get)


def find_power_level(serial_number, x_coord, y_coord):
    """
    The power level is calculated as such:
        -Find the fuel cell's rack ID, which is its X coordinate plus 10.
        -Begin with a power level of the rack ID times the Y coordinate.
        -Increase the power level by the value of the grid serial number (puzzle input)
        -Set the power level to itself multiplied by the rack ID.
        -Keep only the hundreds digit of the power level
        -Subtract 5 from the power level.
    :param serial_number: the puzzle input
    :param x_coord:
    :param y_coord:
    :return: the integer power level
    """
    rack_id = x_coord + 10
    power_level = rack_id * y_coord
    power_level += serial_number
    power_level *= rack_id
    power_level = int(str(power_level)[-3 ]) if power_level >= 100 else 0
    power_level -= 5
    return power_level


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 11.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))