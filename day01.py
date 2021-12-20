from typing import List


def number_increases(depth_measurements: List) -> int:
    count = 0
    first = True
    last_depth = 0
    for depth in depth_measurements:
        if not first and depth > last_depth:
            count += 1
        if first:
            first = False
        last_depth = depth
    return count


def compare_groups(depth_measurements: List) -> int:
    count = 0
    group_a = 0
    back_three = -1
    back_two = -1
    back_one = -1
    for depth in depth_measurements:
        if back_two > 0:
            group_a = depth + back_one + back_two
        if back_three > 0:
            group_b = back_one + back_two + back_three
            if group_a > group_b:
                count += 1
        back_three = back_two
        back_two = back_one
        back_one = depth
    return count
