from utility import convert_input_to_string
import re
from datetime import datetime
import collections


def part1(puzzle_input):
    """
    In the text input file, each line shows a date and time, as well as an action (guard begins shift, wakes up, or
    falls asleep. Part 1 parses the input and finds the guard with the most minutes asleep, and the minute that he is
    most frequent asleep.

    :param puzzle_input:
    :return: the guard ID with the most minutes asleep multiplied by the minute that he is most frequent asleep
    """

    puzzle_input_arr = puzzle_input.strip().split('\n')
    seconds_to_action = {}  # {timestamp: (datetime, action)}
    for line in puzzle_input_arr:
        m = re.match(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\](.*)', line)
        dt = datetime(1970, int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        seconds = dt.timestamp()
        seconds_to_action[seconds] = (dt, m.group(6))
    seconds_sorted = sorted(seconds_to_action.keys())
    guard_to_minutes_slept = {}  # {guard ID: number of minutes slept}
    guard_to_minute = {}  # {Guard ID: [5, 6, 7, 8, 9...24, 30, 31...54, 24, 25, 26, 27, 28]}
    for second in seconds_sorted:
        dt, action = seconds_to_action[second]
        if "begins" in action:
            guard_id = int(re.match(r' Guard #(\d+)', action).group(1))
            if guard_id not in guard_to_minutes_slept:  # I could use a default dictionary for this
                guard_to_minutes_slept[guard_id] = 0
                guard_to_minute[guard_id] = []
        elif "falls" in action:
            sleep_time = dt
        elif "wakes" in action:
            difference_in_minutes = int((dt.timestamp() - sleep_time.timestamp()) // 60)
            guard_to_minutes_slept[guard_id] += difference_in_minutes
            guard_to_minute[guard_id] += [(sleep_time.minute + i) % 60 for i in range(difference_in_minutes)]
    guard_with_longest_sleep = max(guard_to_minutes_slept, key=guard_to_minutes_slept.get)
    most_common_minute = max(guard_to_minute[guard_with_longest_sleep],
                             key=guard_to_minute[guard_with_longest_sleep].count)
    return guard_with_longest_sleep * most_common_minute


def part2(puzzle_input):
    """
    In the text input file, each line shows a date and time, as well as an action (guard begins shift, wakes up, or
    falls asleep. Part 2 parses the input and finds the guard who is the most frequently asleep on the same minute. Same
    code as part 1 except there is extra dictionary to keep track of who is asleep for each minute and extra
    functionality to parse it.

    :param puzzle_input:
    :return: the guard ID who is the most frequently asleep on the same minute multiplied by that minute
    """

    puzzle_input_arr = puzzle_input.split('\n')
    seconds_to_action = {}  # {timestamp: (datetime, action)
    for line in puzzle_input_arr:
        m = re.match(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\](.*)', line)
        dt = datetime(1970, int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        seconds = dt.timestamp()
        seconds_to_action[seconds] = (dt, m.group(6))
    seconds_sorted = sorted(seconds_to_action.keys())
    guard_to_minutes_slept = {}  # {Guard ID: number of minutes slept}
    guard_to_minute = {}  # {Guard Id: [5, 6, 7, 8, 9...24, 30, 31...54, 24, 25, 26, 27, 28]}
    minute_to_guard_slept= {}  # {minute: [guard IDs]}
    guard_id = 0
    sleep_time = None
    for second in seconds_sorted:
        dt, action = seconds_to_action[second]
        if "begins" in action:
            guard_id = int(re.match(r' Guard #(\d+)', action).group(1))
            if guard_id not in guard_to_minutes_slept:
                guard_to_minutes_slept[guard_id] = 0
                guard_to_minute[guard_id] = []
        elif "falls" in action:
            sleep_time = dt
        elif "wakes" in action:
            difference_in_minutes = int((dt.timestamp() - sleep_time.timestamp()) // 60)
            guard_to_minutes_slept[guard_id] += difference_in_minutes
            for i in range(difference_in_minutes):
                if (sleep_time.minute + i) % 60 not in minute_to_guard_slept:
                    minute_to_guard_slept[(sleep_time.minute + i) % 60] = [guard_id]
                else:
                    minute_to_guard_slept[(sleep_time.minute + i) % 60].append(guard_id)
    most_frequent_number_of_occurrences, sleepiest_guard_id = (0, 0)
    sleepiest_minute = 0
    for minute in minute_to_guard_slept:
        c = collections.Counter(minute_to_guard_slept[minute])
        if c.most_common(1)[0][1] > most_frequent_number_of_occurrences:
            sleepiest_guard_id, most_frequent_number_of_occurrences = c.most_common(1)[0]
            sleepiest_minute = minute
    return sleepiest_guard_id * sleepiest_minute


if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 4.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))