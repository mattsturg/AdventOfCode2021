import pytest
import day03


@pytest.fixture
def sample_list():
    return ["00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010"]


def test_day03_sample(sample_list):
    assert day03.binary_count(sample_list) == 198


def test_day03_part_two_sample(sample_list):
    assert day03.binary_count_two(sample_list) == 230


@pytest.fixture
def real_list():
    filename = "testData/day03_test.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line.rstrip())
    return return_list


def test_day03(real_list):
    assert day03.binary_count(real_list) == 1458194


def test_day03_part_two(real_list):
    assert day03.binary_count_two(real_list) == 2829354
