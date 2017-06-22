import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#New chrome driver
def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver

def linked_in_login(driver):
    driver.get("http://www.linkedin.com")
    try:
        name_field = driver.find_element_by_class_name("login-email")
        name_field.send_keys(email)
        time.sleep(1)

        pw_field = driver.find_element_by_class_name("login-password")
        pw_field.send_keys(password)
        time.sleep(1)

        submit_button = driver.find_element_by_id("login-submit").click()

    except NoSuchElementException:
        print 'No such element! '
        driver.quit()

def execute_task(task_list, task, driver):
    execute_operation_list(task_list[task])

def execute_operation_list(operation_list, driver):
    for operation_type, value in operation_list.iteritems():
        if operation_type == '$link':
            driver.get(value)
        elif operation_type == '$class':
            driver.find_element_by_class_name(value).click()
        elif operation_type == '$id':
            driver.find_element_by_id(value).click()

#main
driver = init_driver()





