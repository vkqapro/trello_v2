import pytest

from src.helpers.requestAPI import Api_Calls

class BaseTest:
    API: Api_Calls
    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.API = Api_Calls()

