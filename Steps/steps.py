import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@given("Navigate to {url}")
def Open_Web_browser(context, url):
    context.driver.get("https://fa-evzi-test-saasfaprod1.fa.ocs.oraclecloud.com/")


@then('Insert in "{field}": "{value}"')
def insert_data(context, field, value):
    if field == "Username":
        context.driver.find_element(By.ID, "userid").send_keys(value)
    elif field == "Password":
        context.driver.find_element(By.ID, "password").send_keys(value)
    elif field == "Title":
        context.driver.find_element(By.XPATH, "//td[@class='x18u']//input[@class='x25']").send_keys(value)


@then('Click on "{btn}" button')
def click_on_btn(context, btn):
    if btn == "Login":
        context.driver.find_element(By.ID, "btnActive").click()
    elif btn == "Home":
        context.driver.find_element(By.XPATH, "//a[@title='Home']").click()
    elif btn == "Sales":
        context.driver.find_element(By.ID, "groupNode_sales").click()
    elif btn == "Service Request":
        context.driver.find_element(By.CSS_SELECTOR, "#itemNode_sales_service_requests").click()
    elif btn == "Create Service Request":
        context.driver.find_element(By.XPATH, "//button[@title='Create Service Request']").click()
    elif btn == "Save and Close":
        context.driver.find_element(By.XPATH, "//button[@title='Save and Close']").click()
    elif btn == "list arrow":
        context.driver.find_element(By.XPATH, "(//a[@class='x1kr'])[1]").click()
    time.sleep(5)


@then('Choose "{optn}" option')
def choose_Option(context, optn):
    if optn == "English language":
        drop = Select(context.driver.find_element(By.TAG_NAME, "select"))
        drop.select_by_value("en-us")
    if optn == "Open Service Requests Created By Me":
        context.driver.find_element(By.XPATH, "//li[@_adfiv='2']").click()


@when('"Sales" button is visible')
def verify_Btn_visible(context):
    while not context.driver.find_element(By.CSS_SELECTOR, "#groupNode_sales").is_displayed():
        context.driver.find_element(By.ID, "clusters-right-nav").click()
        time.sleep(2)


@then("Verify that the Service Request has been created")
def Creation_Verification(context):
    context.driver.find_element(By.XPATH, "(//span[text()='Sales and Support 2023'])[1]").is_displayed()
