from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Driver:
    def driver_setup(self):
        driver = webdriver.Chrome()
        return driver

    def wait_until(self, driver, timeout):
        wait = WebDriverWait(driver=driver, timeout=timeout)
        return wait



