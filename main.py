#pip install selenium
#pip install webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import platform


class Driver:
    driver = None

    def __init__(self, not_window=False):
        os_info = platform.system()
        if os_info == 'Windows':
            op = webdriver.ChromeOptions()
            if not_window:
                op.add_argument('headless')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
            self.driver = driver

        elif os_info == 'Linux':
            op = Options()

            if not_window:
                op.headless = True
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=op)
            self.driver = driver


driver = Driver(not_window=True).driver

driver.get("http://google.com")

print(driver.current_url)
print(driver.title)

driver.close()
