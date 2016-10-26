from hamcrest import assert_that, equal_to
import pytest


@pytest.mark.usefixtures('config')
def test_addoptions(config):
    assert_that(config.base_url, equal_to("http://127.0.0.1"))
    assert_that(config.myprop, equal_to("myprop_value"))
    assert_that(config.mysqldb, equal_to("mydb"))

