import pytest
import day01


@pytest.fixture
def sample_list():
    return [199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263]


def test_day01_sample(sample_list):
    assert day01.number_increases(sample_list) == 7


def test_day01_part_two_sample(sample_list):
    assert day01.compare_groups(sample_list) == 5


@pytest.fixture
def real_list():
    filename = "testData/day01_test.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(int(line))
    return return_list


def test_day01(real_list):
    assert day01.number_increases(real_list) == 1233


def test_day01_part_two(real_list):
    assert day01.compare_groups(real_list) == 1275
