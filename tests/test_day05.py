import pytest
import day05


@pytest.fixture
def sample_list():
    filename = "testData/day05_test_sample.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line.rstrip())
    return return_list


def test_day05_sample(sample_list):
    assert day05.grid_building(sample_list) == 5


def test_day05_part_two_sample(sample_list):
    assert day05.grid_building_with_diagonals(sample_list) == 12


@pytest.fixture
def real_list():
    filename = "testData/day05_test.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line.rstrip())
    return return_list


def test_day05(real_list):
    assert day05.grid_building(real_list) == 4993


def test_day05_part_two(real_list):
    assert day05.grid_building_with_diagonals(real_list) == 21101
