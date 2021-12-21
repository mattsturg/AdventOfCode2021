from typing import List


def binary_count(numbers: List) -> int:
    size = len(numbers[0])
    count_bits = [0] * size
    count_strings = 0
    for binary in numbers:
        count_strings += 1
        for i in range(0, size):
            if int(binary[i]):
                count_bits[i] = int(count_bits[i])+1
    count_strings /= 2
    gamma = [0] * size
    epsilon = [0] * size
    index = 0
    for bit in count_bits:
        if int(bit) > count_strings:
            gamma[index] = '1'
            epsilon[index] = '0'
        else:
            gamma[index] = '0'
            epsilon[index] = '1'
        index += 1
    return int("".join(gamma), 2) * int("".join(epsilon), 2)


def split_least_most(numbers: List, index: int):
    ones = []
    zeros = []
    for binary in numbers:
        if int(binary[index]):
            ones.append(binary)
        else:
            zeros.append(binary)
    if len(ones) >= len(zeros):
        return ones, zeros
    else:
        return zeros, ones


def calc_oxygen(possibilities: List) -> int:
    for i in range(1, len(possibilities[0])):
        temp = split_least_most(possibilities, i)[0]
        if len(temp) == 0:
            return possibilities[len(possibilities)-1]
        else:
            possibilities = temp
    return possibilities[len(possibilities)-1]


def calc_co_two(possibilities: List) -> int:
    for i in range(1, len(possibilities[0])):
        temp = split_least_most(possibilities, i)[1]
        if len(temp) == 0:
            return possibilities[len(possibilities)-1]
        else:
            possibilities = temp
    return possibilities[len(possibilities)-1]


def binary_count_two(numbers: List) -> int:
    more, less = split_least_most(numbers, 0)
    oxygen_generation = calc_oxygen(more)
    co_two_scrubber = calc_co_two(less)
    return int(oxygen_generation, 2) * int(co_two_scrubber, 2)
