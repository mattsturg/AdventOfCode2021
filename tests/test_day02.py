import pytest
import day02


@pytest.fixture
def sample_list():
    return ["forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"]


def test_day02_sample(sample_list):
    assert day02.multiply(sample_list) == 150


def test_day02_part_two_sample(sample_list):
    assert day02.aim_multiply(sample_list) == 900


@pytest.fixture
def real_list():
    filename = "testData/day02_test.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


def test_day02(real_list):
    assert day02.multiply(real_list) == 2070300


def test_day02_part_two(real_list):
    assert day02.aim_multiply(real_list) == 2078985210