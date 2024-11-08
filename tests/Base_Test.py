from src.helpers.requestAPI import API_Calls

import pytest

class BaseTest:
    API: API_Calls

    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.API = API_Calls()
