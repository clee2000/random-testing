import random
import pytest


def test1():
    assert random.randint(1, 2) == 2


def test2():
    assert True


def test3():
    assert random.randint(1, 2) == 2


def test4():
    assert random.randint(1, 2) == 2


@pytest.fixture(scope="class")
def dummy_data(request):
    request.cls.num1 = 10
    request.cls.num2 = 20
    print("Execute fixture")


@pytest.mark.usefixtures("dummy_data")
class TestCalculatorClass:
    def test_distance(self):
        print("Test distance function")
        assert True

    def test_sum_of_square(self):
        print("Test sum of square function")
        assert random.randint(1, 2) == 2
