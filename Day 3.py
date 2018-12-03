from utility import convert_input_to_string
import re


def part1(puzzle_input):
    puzzle_input_arr = puzzle_input.split('\n')
    visited_squares = {}
    overlapped_squares = set()
    overlap_number = 0
    for line in puzzle_input_arr:
        line_elements = re.split('#[0-9]+ @|:|,|x', line)
        x_coord = int(line_elements[1])
        y_coord = int(line_elements[2])
        width = int(line_elements[3])
        height = int(line_elements[4])
        for i in range(width):
            for j in range(height):
                if (i + x_coord, j + y_coord) not in visited_squares:
                    visited_squares[(i + x_coord, j + y_coord)] = 1
                else:
                    visited_squares[(i + x_coord, j + y_coord)] += 1
                    if (i + x_coord, j + y_coord) not in overlapped_squares:
                        overlapped_squares.add((i + x_coord, j + y_coord))
                        overlap_number += 1
    return overlap_number


def part2(puzzle_input):
    puzzle_input_arr = puzzle_input.split('\n')
    visited_squares = {}
    all_claims = set()
    overlapped = set()
    for line in puzzle_input_arr:
        line_elements = re.split('[#@:,x]', line)
        claim = int(line_elements[1])
        x_coord = int(line_elements[2])
        y_coord = int(line_elements[3])
        width = int(line_elements[4])
        height = int(line_elements[5])
        all_claims.add(claim)
        for i in range(width):
            for j in range(height):
                if (i + x_coord, j + y_coord) not in visited_squares:
                    visited_squares[(i + x_coord, j + y_coord)] = claim
                else:
                    overlapped.add(visited_squares[(i + x_coord, j + y_coord)])
                    overlapped.add(claim)
    return list(all_claims.difference(overlapped))[0]


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 3.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))