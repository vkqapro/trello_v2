import pytest
import logging as log
from src.helpers.requestAPI import API_Call


@pytest.mark.hc
def test_healthcheck():
    log.info('Hello World!!')
    log.info('Hello World!!')
    r = API_Call()
    r = r.get_call()
    log.info("+" * 100)
    log.info(r.json())