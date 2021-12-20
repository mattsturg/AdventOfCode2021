import pytest
import day01


@pytest.fixture
def sampleList():
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





def test_day_01_sample(sampleList):
    assert day01.numberIncreases(sampleList) == 7

def testDay01Part2Sample(sampleList):
        assert day01.compareGroups(sampleList) == 5

@pytest.fixture
def realList():
        filename = "testData/day01Test1.txt"
        realList = []
        with open(filename, 'r') as fileHandle:
                for line in fileHandle:
                        realList.append(int(line))
        return realList

def testDay01(realList):
        assert day01.numberIncreases(realList) == 1233

def testDay01P2(realList):
        assert day01.compareGroups(realList) == 1275