from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import platform
import pickle

class MyDriver:
    driver = None

    def __init__(self, not_window=False):
        os_info = platform.system()
        if os_info == 'Windows':
            op = webdriver.ChromeOptions()
            if not_window:
                op.add_argument("--headless")
            op.add_argument("--incognito")
            op.add_argument('--no-sandbox')
            op.add_argument('window-size=1051x806')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
            self.driver = driver

        elif os_info == 'Linux':
            op = Options()

            if not_window:
                op.headless = True
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=op)
            self.driver = driver


    def salvar_sessao(self):
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

    def carregar_sessao(self):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

