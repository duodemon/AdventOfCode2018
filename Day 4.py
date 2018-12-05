from utility import convert_input_to_string
import re
import time
from datetime import datetime
import collections


def part1(puzzle_input):
    puzzle_input_arr = puzzle_input.split('\n')
    '''
      {
        timestamp: (datetime, action)
      }
    '''
    seconds_to_action = {}
    for line in puzzle_input_arr:
        m = re.match(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\](.*)', line)
        dt = datetime(1970, int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        seconds = dt.timestamp()
        seconds_to_action[seconds] = (dt, m.group(6))
    seconds_sorted = sorted(seconds_to_action.keys())

    '''
      {
        'GuardId': sum
      }
    '''
    guard_to_minutes_slept = {}

    '''
      {
        'GuardId': [5, 6, 7, 8, 9...24, 30, 31...54, 24, 25, 26, 27, 28]
      }
    '''
    guard_to_minute = {}
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
            guard_to_minute[guard_id] += [(sleep_time.minute + i) % 60 for i in range(difference_in_minutes)]
    print(guard_to_minutes_slept)
    guard_with_longest_sleep = max(guard_to_minutes_slept, key=guard_to_minutes_slept.get)
    print(guard_with_longest_sleep)
    most_common_minute = max(guard_to_minute[guard_with_longest_sleep],
                             key=guard_to_minute[guard_with_longest_sleep].count)
    print(most_common_minute)
    return guard_with_longest_sleep * most_common_minute


def part2(puzzle_input):
    puzzle_input_arr = puzzle_input.split('\n')
    '''
      {
        timestamp: (datetime, action)
      }
    '''
    seconds_to_action = {}
    for line in puzzle_input_arr:
        m = re.match(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\](.*)', line)
        dt = datetime(1970, int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        seconds = dt.timestamp()
        seconds_to_action[seconds] = (dt, m.group(6))
    seconds_sorted = sorted(seconds_to_action.keys())

    '''
      {
        'GuardId': sum
      }
    '''
    guard_to_minutes_slept = {}

    '''
      {
        'GuardId': [5, 6, 7, 8, 9...24, 30, 31...54, 24, 25, 26, 27, 28]
      }
    '''
    guard_to_minute = {}
    '''
      {
        'minute': [guardIDs]
      }
    '''
    minute_to_guard_slept= {}
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
    print(minute_to_guard_slept)
    most_frequent_number_of_occurrences, sleepiest_guard_id = (0, 0)
    sleepiest_minute = 0
    for minute in minute_to_guard_slept:
        c = collections.Counter(minute_to_guard_slept[minute])
        if c.most_common(1)[0][1] > most_frequent_number_of_occurrences:
            sleepiest_guard_id, most_frequent_number_of_occurrences = c.most_common(1)[0]
            sleepiest_minute = minute
        print(sleepiest_guard_id, most_frequent_number_of_occurrences  )
    return sleepiest_guard_id * sleepiest_minute

if __name__ == "__main__":
    puzzle_input = convert_input_to_string("Day 4.txt")
    #print(part1(puzzle_input))
    print(part2(puzzle_input))