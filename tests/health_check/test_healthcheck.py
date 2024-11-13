from tests.Base_Test import BaseTest

import pytest
import logging as log

class TestHC(BaseTest):
    @pytest.mark.hc
    def test__hc(self):
        log.info('+' * 50)
        log.info(self.API.GET(200))