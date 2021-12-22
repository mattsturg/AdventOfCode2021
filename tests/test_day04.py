import pytest
import day04


@pytest.fixture
def sample_list():
    filename = "testData/day04_test_sample.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line.rstrip())
    return return_list


def test_day04_sample(sample_list):
    assert day04.bingo(sample_list) == 4512


def test_day04_part_two_sample(sample_list):
    assert day04.bingo_loose(sample_list) == 1924


@pytest.fixture
def real_list():
    filename = "testData/day04_test.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line.rstrip())
    return return_list


def test_day04(real_list):
    assert day04.bingo(real_list) == 25410


def test_day04_part_two(real_list):
    assert day04.bingo_loose(real_list) == 2730
