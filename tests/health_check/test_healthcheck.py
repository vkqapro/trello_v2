from tests.Base_Test import BaseTest

import pytest
import logging as log
import time
from selenium.webdriver.common.by import By


class TestHC(BaseTest):
    @pytest.mark.hc
    def test__hc(self):
        log.info('+' * 50)
        log.info(self.API.GET(200))

class Test_UI(BaseTest):
    user_name = 'vkqa.pro@gmail.com'
    user_password = 'Password1!'
    @pytest.mark.login
    def test_login(self):
        driver = self.Driver.driver_setup()
        wait = self.Driver.wait_until(driver=driver, timeout=60)
        user_type_text = 'STUDENT'
        driver.get('http://ask.portnov.com/#/login')
        time.sleep(2)
        el_login_username = driver.find_element(By.XPATH, "//input[@id='mat-input-0']")
        el_login_password = driver.find_element(By.XPATH, "//input[@id='mat-input-1']")
        el_login_signin_button = driver.find_element(By.XPATH, "//body/ac-root[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/ac-login-page[1]/mat-card[1]/form[1]/div[1]/button[1]")

        if el_login_username.is_displayed():
            el_login_username.click()
            el_login_username.send_keys(self.user_name)
            el_login_password.click()
            el_login_password.send_keys(self.user_password)
            el_login_signin_button.click()
            time.sleep(3)
            get_text = wait.until(lambda d: driver.find_element(By.XPATH, "//p[contains(text(),'STUDENT')]"))
            log.info('=' * 50)
            log.info(f"The returned element text is: {get_text.text} and expected text is: {user_type_text}")

            assert get_text.text == f"{user_type_text}", "Element is not found"
            driver.quit()

        else:
            raise Exception(f"Element is not found")


