from utility import convert_input_to_string
from collections import defaultdict
import re


def addr(registers, A, B, C):
    registers[C] = registers[A] + registers[B]
    return registers


def addi(registers, A, B, C):
    registers[C] = registers[A] + B
    return registers


def mulr(registers, A, B, C):
    registers[C] = registers[A] + registers[B]
    return registers


def muli(registers, A, B, C):
    registers[C] = registers[A] + B
    return registers


def banr(registers, A, B, C):
    registers[C] = registers[A] & registers[B]
    return registers


def bani(registers, A, B, C):
    registers[C] = registers[A] & B
    return registers


def borr(registers, A, B, C):
    registers[C] = registers[A] | registers[B]
    return registers


def bori(registers, A, B, C):
    registers[C] = registers[A] | registers[B]
    return registers


def setr(registers, A, B, C):
    registers[C] = registers[A]
    return registers


def seti(registers, A, B, C):
    registers[C] = A


def gtir(registers, A, B, C):
    registers[C] = 1 if A > registers[B] else 0
    return registers


def gtri(registers, A, B, C):
    registers[C] = 1 if registers[A] > B else 0
    return registers


def gtrr(registers, A, B, C):
    registers[C] = 1 if registers[A] > registers[B] else 0
    return registers


def eqir(registers, A, B, C):
    registers[C] = 1 if A == registers[B] else 0
    return registers


def eqri(registers, A, B, C):
    registers[C] = 1 if registers[A] == B else 0
    return registers


def eqrr(registers, A, B, C):
    registers[C] = 1 if registers[A] == registers[B] else 0
    return registers


opcode_functions = {
    'addr': lambda *args: addr(*args),
    'addi': lambda *args: addi(*args),
    'mulr': lambda *args: mulr(*args),
    'muli': lambda *args: muli(*args),
    'banr': lambda *args: banr(*args),
    'bani': lambda *args: bani(*args),
    'borr': lambda *args: borr(*args),
    'bori': lambda *args: bori(*args),
    'setr': lambda *args: setr(*args),
    'seti': lambda *args: seti(*args),
    'gtir': lambda *args: gtir(*args),
    'gtri': lambda *args: gtri(*args),
    'gtrr': lambda *args: gtrr(*args),
    'eqir': lambda *args: eqir(*args),
    'eqri': lambda *args: eqri(*args),
    'eqrr': lambda *args: eqrr(*args),
}

def part1(puzzle_input):
    """
    There is a device that has four registers and can be manipulated by 16 different opcodes (all defined above). In the
    first part of the text file input, there are before and after states for the four registers upon executed by an opcode
    and its three parameters.

    Part 1 finds the number of samples in the puzzle input that behaves like three or more opcodes.
    :param puzzle_input:
    :return: the number of samples that behaves like three or more opcodes.
    """
    part1_input = puzzle_input.strip().split("\n\n\n")[0]
    part1_input_arr = part1_input.split("\n\n")
    samples_behaving_like_three_or_more_opcodes_count = 0
    for sample in part1_input_arr:
        working_opcodes = 0
        integers = list(re.findall('(\d+)', sample))
        integers = [int(i) for i in integers]
        before_registers = integers[:4]
        instructions = integers[4:8]
        after_registers = integers[8:]
        for opcode_function in opcode_functions:
            result_registers = opcode_functions[opcode_function](before_registers.copy(), instructions[1], instructions[2], instructions[3])
            if result_registers == after_registers:
                working_opcodes += 1
            if working_opcodes == 3:
                samples_behaving_like_three_or_more_opcodes_count += 1
                break
    return samples_behaving_like_three_or_more_opcodes_count


def part2(puzzle_input):
    """
    There is a device that has four registers and can be manipulated by 16 different opcodes (all defined above). In the
    first part of the text file input, there are before and after states for the four registers upon executed by an opcode
    and its three parameters.

    The second part of the text file input has a sample program that alters the four registers, which each have an initial
    value of 0.

    Part 2 assigns a number to each opcode and executes the program and finds the value in the first register.
    :param puzzle_input:
    :return: the value of register 0 upon executing the program
    """

    # Identifying the opcode numbers
    part2_input = puzzle_input.strip().split("\n\n\n")[0]
    part2_input_arr = part2_input.split("\n\n")
    opcodes = {}
    while len(opcodes) != 16:
        for sample in part2_input_arr:
            sample_opcodes = []
            integers = list(re.findall('(\d+)', sample))
            integers = [int(i) for i in integers]
            before_registers = integers[:4]
            instructions = integers[4:8]
            after_registers = integers[8:]
            for opcode_function in opcode_functions:
                result_registers = opcode_functions[opcode_function](before_registers.copy(), instructions[1], instructions[2], instructions[3])
                if result_registers == after_registers and opcode_function not in opcodes.values():
                    sample_opcodes.append(opcode_function)
            if len(sample_opcodes) == 1:
                opcodes[instructions[0]] = sample_opcodes[0]

    # Executing the sample program
    execution_instructions = puzzle_input.strip().split("\n\n\n")[1]
    registers = [0, 0, 0, 0]
    for instruction in execution_instructions.strip().split("\n"):
        params = instruction.split(" ")
        opcode_functions[opcodes[params[0]]](registers, params[1], params[2], params[3])
    return registers[0]


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 16.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))