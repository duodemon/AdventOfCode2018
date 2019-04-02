from utility import convert_input_to_string
import re
from collections import defaultdict

alphabet = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1(puzzle_input):
    """
    Each line in the text file input contains information about each step that must be finished before another step. Part
    1 finds the order that the steps must be taken.

    :param puzzle_input:
    :return: a string depicting the order of the steps
    """
    letters_to_pointing_to = defaultdict(list)
    letters_to_pointed_by = defaultdict(list)
    puzzle_input_arr = puzzle_input.strip().split('\n')
    for line in puzzle_input_arr:
        m = re.match('Step (\w).+step (\w)', line)
        letters_to_pointing_to[m.group(1)].append(m.group(2))
        letters_to_pointed_by[m.group(2)].append(m.group(1))
    queue = ['T', 'V', 'G', 'K']
    result_string = ""
    while queue:
        queue.sort()
        current_letter = queue.pop(0)
        result_string += current_letter
        for dependency in letters_to_pointing_to[current_letter]:
            if len(set(letters_to_pointed_by[dependency]).difference(set(result_string))) == 0:
                queue.append(dependency)
    return result_string


def part2(puzzle_input):
    """
    Each line in the text file input contains information about each step that must be finished before another step. In
    part 2, there are five workers and each step takes n seconds to complete, where n corresponds to the letter value
    (A=1, Z=26). Once a task is finished, the worker moves onto the next available task. Part 2 finds the total time it
    takes for all tasks to finish.

    :param puzzle_input:
    :return: the total time for all steps to finish
    """
    letters_to_pointing_to = defaultdict(list)
    letters_to_pointed_by = defaultdict(list)
    puzzle_input_arr = puzzle_input.strip().split('\n')
    for line in puzzle_input_arr:
        m = re.match('Step (\w).+step (\w)', line)
        letters_to_pointing_to[m.group(1)].append(m.group(2))
        letters_to_pointed_by[m.group(2)].append(m.group(1))
    worker1, worker2, worker3, worker4, worker5 = Worker(), Worker(), Worker(), Worker(), Worker()
    workers = [worker1, worker2, worker3, worker4, worker5]
    queue = ['T', 'V', 'G', 'K']
    worker_queue = workers[:]
    total_time = 0
    while queue or len(worker_queue) != 5:
        while queue and worker_queue:
            queue.sort()
            current_worker = worker_queue.pop(0)
            current_letter = queue.pop(0)
            current_worker.receive_letter(current_letter)
        for worker in workers:
            worker.tick(queue, worker_queue, letters_to_pointing_to, letters_to_pointed_by)
        total_time += 1
    return total_time


class Worker:

    result_string = ""

    def __init__(self):
        self.letter = ''
        self.time = 0

    def receive_letter(self, letter):
        self.letter = letter
        self.time = 60 + alphabet.index(letter)

    def tick(self, queue, worker_queue, letters_to_pointing_to, letters_to_pointed_by):
        self.time -= 1
        if self.time == 0:
            worker_queue.append(self)
            Worker.result_string += self.letter
            for dependency in letters_to_pointing_to[self.letter]:
                if len(set(letters_to_pointed_by[dependency]).difference(set(Worker.result_string))) == 0:
                    queue.append(dependency)


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 7.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))