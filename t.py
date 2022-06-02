import unittest
import random
import expecttest
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    print(item.execution_count)
    print(";alksdfja;lkdfj")


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

    @pytest.mark.skipif(2 == 2, reason="no way of currently testing this")
    def test_sum_of_square(self):
        print("Test sum of square function")
        assert random.randint(1, 2) == 2


class TestCase(expecttest.TestCase):
    def run(self, result=None):
        print("hello")
        super().run(result=result)
        print(result)


class Testing(TestCase):
    def test_unittest_1(self):
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        self.assertEqual(a, b)

    # @unittest.skip("al;sdkfj")
    def test_unittest_2(self):
        a = True
        b = True
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
