from  tests.Base_Test import BaseTest

import pytest
import logging as log

class TestHC(BaseTest):
    @pytest.mark.hc
    def test_hc(self):
        request = self.API
        log.info('Hello World')
        log.info('=' * 50)
        log.info(request.GET().status_code)
        log.info('=' * 50)
        log.info(request.GET().json())


