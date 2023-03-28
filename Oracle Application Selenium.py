from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set chrome options and service object
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
service_obj = Service(ChromeDriverManager().install())

# Create chrome webdriver object
driver = webdriver.Chrome(service=service_obj, options=chrome_option)

# Open the Oracle login page and set language to English
driver.get("https://fa-evzi-test-saasfaprod1.fa.ocs.oraclecloud.com/")
driver.maximize_window()
drop = Select(driver.find_element(By.TAG_NAME, "select"))
drop.select_by_value("en-us")

# Log in to the Oracle cloud with provided user ID and password
driver.find_element(By.ID, "userid").send_keys("QA.001")
driver.find_element(By.ID, "password").send_keys("SeFusionTestOC00#@!@&")
driver.find_element(By.ID, "btnActive").click()
time.sleep(2)

# Navigate to the Home page
driver.find_element(By.XPATH, "//a[@title='Home']").click()
time.sleep(5)


while not driver.find_element(By.CSS_SELECTOR, "#groupNode_sales").is_displayed():
    driver.find_element(By.ID, "clusters-right-nav").click()
    time.sleep(2)
driver.find_element(By.ID, "groupNode_sales").click()

driver.find_element(By.CSS_SELECTOR, "#itemNode_sales_service_requests").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[@title='Create Service Request']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//td[@class='x18u']//input[@class='x25']").send_keys("Samana's Sales and Support Staff")
time.sleep(5)

# ========================================================================= #
driver.find_element(By.XPATH, "//button[@title='Save and Close']").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//a[@class='x1kr'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//li[@_adfiv='2']").click()

