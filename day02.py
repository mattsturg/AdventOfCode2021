from typing import List


def multiply(movements: List) -> int:
    x = 0
    y = 0
    for text in movements:
        split_str = text.split()
        if split_str[0] == "forward":
            x += int(split_str[1])
        elif split_str[0] == "down":
            y += int(split_str[1])
        elif split_str[0] == "up":
            y -= int(split_str[1])
    return x*y


def aim_multiply(movements: List) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for text in movements:
        split_str = text.split()
        if split_str[0] == "forward":
            horizontal += int(split_str[1])
            depth += aim * int(split_str[1])
        elif split_str[0] == "down":
            aim += int(split_str[1])
        elif split_str[0] == "up":
            aim -= int(split_str[1])
    return horizontal*depth
