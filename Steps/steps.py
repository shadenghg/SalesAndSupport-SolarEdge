import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import logging


@given('Navigate to the website "{url}"')
def Open_Web_browser(context, url):
    logging.info(f"Opening web browser and navigating to {url}")
    context.driver.get(url)


@then('Insert in "{field}": "{value}"')
def insert_data(context, field, value):
    if field == "Username":
        context.driver.find_element(By.ID, "userid").send_keys(value)
        logging.info(f"Inserted username: {value}")
    elif field == "Password":
        context.driver.find_element(By.ID, "password").send_keys(value)
        logging.info("Inserted password: ********")
    elif field == "Title":
        context.driver.find_element(By.XPATH, "//td[@class='x18u']//input[@class='x25']")\
            .send_keys(value)
        logging.info(f"Inserted title: {value}")
    elif field == "Subject":
        context.driver.find_element(By.XPATH, "//input[@aria-label='Subject']")\
            .send_keys(value)
        logging.info(f"Inserted subject: {value}")


@then('Click on "{buttons}" button')
def click_add(context, buttons):
    for button in context.buttons:
        if button[1] == buttons:
            if button[3] == "ID":
                time.sleep(5)
                context.driver.find_element(By.ID, button[2]).click()
                logging.info(f"Clicked on {buttons} button using ID locator")
            elif button[3] == "XPATH":
                time.sleep(5)
                context.driver.find_element(By.XPATH, button[2]).click()
                logging.info(f"Clicked on {buttons} button using XPath locator")
            elif button[3] == "CSS_SELECTOR":
                time.sleep(5)
                context.driver.find_element(By.CSS_SELECTOR, button[2]).click()
                logging.info(f"Clicked on {buttons} button using CSS Selector locator")


@then('Choose "{optn}" option')
def choose_Option(context, optn):
    if optn == "English language":
        drop = Select(context.driver.find_element(By.TAG_NAME, "select"))
        drop.select_by_value("en-us")
        logging.info("Selected English language option")
    if optn == "Open Service Requests Created By Me":
        time.sleep(5)
        context.driver.find_element(By.XPATH, "//li[@_adfiv='2']").click()
        logging.info("Selected Open Service Requests Created By Me option")


@when('"Sales" button is visible')
def verify_Btn_visible(context):
    while not context.driver.find_element(By.CSS_SELECTOR, "#groupNode_sales").is_displayed():
        context.driver.find_element(By.ID, "clusters-right-nav").click()
        time.sleep(2)
    logging.info("Sales button is visible")


@then("Verify that the Service Request has been created")
def Creation_Verification(context):
    context.driver.find_element(By.XPATH, "(//span[text()='Sales and Support 2023'])[1]").is_displayed()
    logging.info("Service Request has been created successfully")


@then("A message is displayed to the user")
def message_displayed(context):
    message = context.driver.find_element(By.XPATH, "//div[.='Error']")
    assert message.text == "Error", "The error message is not displayed"
    logging.info("Error message is displayed to the user")
