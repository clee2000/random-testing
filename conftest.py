
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item: pytest.Item, call):
    print('a;lsdkjfa;lkdsfjs')
    print(item)
    print("laksdjf;alkdsfj;lkads")
    print(item.execution_count)
