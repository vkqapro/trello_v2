import pytest

from src.helpers.requestAPI import Api_Calls
from src.helpers.seleniumWebDriver import Driver

class BaseTest:
    API: Api_Calls
    Driver: Driver
    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.API = Api_Calls()
        request.cls.Driver = Driver()

