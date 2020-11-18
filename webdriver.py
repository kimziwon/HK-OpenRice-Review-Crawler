from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform
is_os_linux = True if platform.system() == 'Linux' else False


def get_web_driver():
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.

    if is_os_linux:
        driver = webdriver.Chrome(executable_path=r"/usr/bin/chromedriver", options=options)
    else:
        driver = webdriver.Chrome(executable_path='/Users/ziwon/executables/chromedriver86', options=options)
    driver.set_window_size(600, 800)
    return driver
