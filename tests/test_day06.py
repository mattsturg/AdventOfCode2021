import pytest
import day06


@pytest.fixture
def sample_list():
    return ['3, 4, 3, 1, 2']


def test_day06_sample(sample_list):
    assert day06.fish_counter_fast(80, sample_list) == 5934


def test_day06_part_two_sample(sample_list):
    assert day06.fish_counter_fast(256, sample_list) == 26984457539


@pytest.fixture
def real_list():
    filename = "testData/day06_test.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line.rstrip())
    return return_list


def test_day06(real_list):
    assert day06.fish_counter_fast(80, real_list) == 358214


def test_day06_part_two(real_list):
    assert day06.fish_counter_fast(256, real_list) == 1622533344325
