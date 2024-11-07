import pytest
import logging as log
from tests.Base_Test import Base_Test


class Test_E2E(Base_Test):

    @pytest.mark.hc
    def test_healthcheck(self):
        log.info('Hello World!!')
        log.info('Hello World!!')
        result = self.API.get_call()

        log.info("==" * 30)
        log.info(result.json())