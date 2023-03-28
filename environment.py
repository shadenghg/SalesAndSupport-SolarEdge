import sqlite3
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.implicitly_wait(15)
    driver.maximize_window()
    context.driver = driver

    # ============================================================= #
    con = sqlite3.connect("vanilla.db")
    cursorObj = con.cursor()
    buttons = cursorObj.fetchall()
    context.buttons = buttons
    cursorObj.execute("SELECT * FROM data_buttons")
    buttons = cursorObj.fetchall()
    context.buttons = buttons

    # ============================================================= #
    log_file = 'C:/Samana/Sales And Support/Reports/behave.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logging.getLogger('').addHandler(file_handler)
