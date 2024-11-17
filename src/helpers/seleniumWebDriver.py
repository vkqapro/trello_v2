from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options




class Driver:
    def driver_setup(self):
        driver = webdriver.Firefox()
        return driver

    def wait_until(self, driver, timeout):
        wait = WebDriverWait(driver=driver, timeout=timeout)
        return wait



