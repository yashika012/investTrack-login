from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    driver_path = r"D:\drivers\chromedriver-win32\chromedriver.exe"

    service = Service(executable_path=driver_path)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver