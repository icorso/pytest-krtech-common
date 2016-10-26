import pytest

from krtech.configuration import TestConfig, ConftestOptions


class OverwrittenTestConfig(TestConfig):
    myprop = "myprop_value"
    mysqldb = "mydb"

tc = OverwrittenTestConfig()
c = ConftestOptions(tc)


def pytest_addoption(parser):
    c.pytest_addoption(parser)


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    return c.pytest_runtest_makereport(item, call, __multicall__)


@pytest.yield_fixture(scope='session')
def config(request):
    op = c.config(request)
    yield op
    op.driver.close()
