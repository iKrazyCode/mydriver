import mydriver
from selenium.webdriver.common.by import By
from time import sleep

mydriver = mydriver.MyDriver(not_window=False)
driver = mydriver.driver
driver.get("http://google.com")



driver.close()

