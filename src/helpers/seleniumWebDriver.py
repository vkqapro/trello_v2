from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options




class Driver:
    def driver_setup(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def wait_until(self, driver, timeout):
        wait = WebDriverWait(driver=driver, timeout=timeout)
        return wait



