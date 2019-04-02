from utility import convert_input_to_string
from collections import defaultdict

metadata = {}

def part1(puzzle_input_arr, value, head_index, children):
    """
    The text file input is a tree. Each node contains a header, which is always at the start and contains two values:
    number of child nodes and number of metadata entries. The node also contains 0 or more child nodes and one or more
    metadata entries (both as specified in the header). Part 1 finds the sum of all the metadata entries recursively.

    :param puzzle_input_arr:
    :param value: sum of all the metadata entries
    :param head_index: the current index of the node
    :param children: {parent index: [children indices]}
    :return:
    """
    index = head_index
    num_children = int(puzzle_input_arr[index])
    num_metadata = int(puzzle_input_arr[index + 1])
    index += 2
    if num_children != 0:
        for i in range(num_children):
            children[head_index].append(index)
            puzzle_input_arr, value, index, children = part1(puzzle_input_arr, value, index, children)
    temp_list=[]
    for i in range(num_metadata):
        value += int(puzzle_input_arr[index + i])
        temp_list.append(int(puzzle_input_arr[index + i]))
    metadata[head_index] = temp_list
    return puzzle_input_arr, value, index + num_metadata, children


def part2(puzzle_input_arr, head_index, metadata_dict, children):
    """
    The text file input is a tree. Each node contains a header, which is always at the start and contains two values:
    number of child nodes and number of metadata entries. The node also contains 0 or more child nodes and one or more
    metadata entries (both as specified in the header). Part 2 finds the sum of all the metadata entries in the root
    node recursively.

    :param puzzle_input_arr:
    :param head_index: current index of node
    :param metadata_dict: {node index: [metadata values]} (received from the first time doing this in part 1)
    :param children: {parent index: [children indices]} (received from the first time doing this in part 1)
    :return:
    """
    value = 0
    index = head_index
    num_children = int(puzzle_input_arr[index])
    num_metadata = int(puzzle_input_arr[index + 1])
    index += 2
    if num_children == 0:
        for i in range(num_metadata):
            value += int(puzzle_input_arr[index + i])
    else:
        metadata_arr = metadata_dict[head_index]
        for metadata in metadata_arr:
            if metadata != 0 and metadata <= num_children:
                value += part2(puzzle_input_arr, children[head_index][metadata - 1], metadata_dict, children)
    return value


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 8.txt")
    puzzle_input_arr = puzzle_input.strip().split(' ')
    res = part1(puzzle_input_arr, 0, 0, defaultdict(list))
    print(res[1])
    children = res[3]
    print(part2(puzzle_input_arr, 0, metadata, children))