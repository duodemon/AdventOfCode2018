def part1_2(puzzle_input):
    """
    There is an initial queue of two and two positions - one position is assigned to each element.
    Elements are added after each iteration by these rules:
        -The value of position 1 added with the value of position 2
        -Each digit becomes a new element in order
        -Each position steps forward through the queue 1 plus the score of the current position's value
        -If they reach the end, they loop back to the beginning

    Part 1 returns the next ten values after the index of the puzzle input

    Part 2 returns the number of elements before the sequence of the puzzle input first appears.

    This function is mostly catered towards part 2. I just put the print statement for part 1 when part 2 is printed
    for appropriateness.
    :param puzzle_input:
    """
    queue = [3, 7]
    current_position_1 = 0
    current_position_2 = 1
    sequence = [0 for i in puzzle_input]
    count = 0
    while 1:
        sum = queue[current_position_1] + queue[current_position_2]
        if sum >= 10:
            queue.append(int(str(sum)[0]))
            del sequence[0]
            sequence.append(int(str(sum)[0]))
            if ''.join([str(c) for c in sequence]) == puzzle_input:
                print(queue[int(puzzle_input): int(puzzle_input) + 10])  # Part 1
                print(count) # Part 2
                return
            queue.append(int(str(sum)[1]))
            del sequence[0]
            sequence.append(int(str(sum)[1]))
            count += 1
        else:
            queue.append(sum)
            del sequence[0]
            sequence.append(int(str(sum)[0]))
        next_position_1 = ((queue[current_position_1] + 1) % (len(queue)) + current_position_1) % len(queue)
        next_position_2 = ((queue[current_position_2] + 1) % (len(queue)) + current_position_2) % len(queue)
        if ''.join([str(c) for c in sequence]) == str(puzzle_input):
            print(queue[int(puzzle_input): int(puzzle_input) + 10])  # Part 1
            print(count)  # Part 2
            return
        current_position_1 = next_position_1
        current_position_2 = next_position_2
        count += 1


if __name__ == "__main__":
    part1_2('165061')