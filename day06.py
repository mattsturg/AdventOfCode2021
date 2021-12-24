from typing import List


def parse_ages(fish_ages: List):
    new_fish_ages = []
    fish_ages = fish_ages[0].split(',')
    for num in fish_ages:
        new_fish_ages.append(int(num))
    return new_fish_ages


def shift(counts: List):
    num = counts.pop(0)
    counts.append(num)
    counts[6] += num


def fish_counter_fast(number_of_days: int, fish_ages: List) -> int:
    fish_ages = parse_ages(fish_ages)
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in fish_ages:
        counts[num] += 1
    for day_num in range(number_of_days):
        shift(counts)
    return sum(counts)
