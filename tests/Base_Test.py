from src.helpers.requestAPI import API_Call

import pytest

class Base_Test:
    API: API_Call
    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.API = API_Call()

