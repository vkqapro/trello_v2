from tests.Base_Test import BaseTest


import re
import time
from playwright.sync_api import Page, expect
import pytest
import logging as log

user_name = 'vkqa.pro@gmail.com'
user_password = 'Password1!'
url = 'http://ask.portnov.com/#/login'
url_home = 'http://ask.portnov.com/#/home'
user_type_student = 'STUDENT'

@pytest.mark.tc100
class Test_Login:
    @pytest.fixture(scope='function', autouse=True)
    def goto(self, page: Page):
        page.goto(url)
        yield
        page.close()

    @pytest.mark.tc101
    def test_login_positive_path(self, page: Page):
        page.get_by_label('Email *').fill(user_name)
        page.get_by_label('Password *').fill(user_password)
        page.get_by_role('button', name=re.compile('Sign In', re.IGNORECASE)).click()
        expect(page).to_have_url(url_home)
        user_type = page.get_by_text('STUDENT')
        expect(user_type).to_have_text(user_type_student)
    @pytest.mark.tc1002
    def test_login_incorrect_username(self, page: Page):
        page.get_by_label('Email *').fill('qwqweqe')
        page.get_by_label('Password *').fill(user_password)
        page.get_by_role('button', name=re.compile('sign in', re.IGNORECASE)).click()
        error_message = page.get_by_text('Should be a valid email address')
        expect(error_message).to_have_text('Should be a valid email address')

    @pytest.mark.tc103
    def test_login_incorrect_password(self, page: Page):
        page.get_by_label('Email *').fill(user_name)
        page.get_by_label('Password *').fill('qweqweqwe')
        page.get_by_role('button', name=re.compile('sign in', re.IGNORECASE)).click()
        error_message = page.locator('xpath=/html[1]/body[1]/div[2]')
        expect(error_message).to_contain_text('Authentication failed. User not found or password does not match ')


class TestApi(BaseTest):
    @pytest.mark.api
    def test_api_healthcheck(self):
        req = self.API.GET(200)
        log.info(req.status_code)



