from utility import convert_input_to_string
from collections import defaultdict
import re
import copy


class Point:

    def __init__(self):
        self.x_coord = 0
        self.y_coord = 0
        self.x_velocity = 0
        self.y_velocity = 0

    def tick(self):
        self.x_coord += self.x_velocity
        self.y_coord += self.y_velocity


def part1_2(puzzle_input):
    """
    Each line in the input text file represents one point and its starting position and velocity (in coordinates/second).
    Every second that passes, the points move at a rate depicted by the velocity. Part 1 prints the message that's shown
    once the points all collide. Part 2 prints the time it takes for the message to collide.
    :param puzzle_input:
    """
    puzzle_input_arr = puzzle_input.strip().split('\n')
    points = []
    for line in puzzle_input_arr:
        matches = re.match(r'position=<[ ]*(\d+|-\d+), [ ]*(\d+|-\d+)> velocity=<[ ]*(\d+|-\d+), [ ]*(\d+|-\d+)>', line)
        point = Point()
        point.x_coord = int(matches.group(1))
        point.y_coord = int(matches.group(2))
        point.x_velocity = int(matches.group(3))
        point.y_velocity = int(matches.group(4))
        points.append(point)
    previous_area = 90000000000000000000
    previous_points = []
    for i in range(20000):
        x_lowest, x_highest, y_lowest, y_highest = 51000, -51000, 51000, -51000
        for point in points:
            point.tick()
            if point.x_coord < x_lowest:
                x_lowest = point.x_coord
            elif point.x_coord > x_highest:
                x_highest = point.x_coord
            elif point.y_coord < y_lowest:
                y_lowest = point.y_coord
            elif point.y_coord > y_highest:
                y_highest = point.y_coord
        area = (y_highest - y_lowest) * (x_highest - x_lowest)
        if area > previous_area:
            x_offset = x_lowest * -1
            y_offset = y_lowest * -1
            test = [['.' for x in range(x_highest - x_lowest +1)] for y in range(y_highest - y_lowest+1)]
            for point in previous_points:
                test[point.y_coord + y_offset ][point.x_coord + x_offset ] = '#'
            for y in test:
                print(''.join([c if c != '.' else '.' for c in y]).strip('.'))  # Part 1, prints out the message
            print('seconds = ' + str(i))  # Part 2, prints out the total time in seconds to reach that message
            return
        else:
            previous_area = area
            previous_points = copy.deepcopy(points)


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 10.txt")
    part1_2(puzzle_input)
