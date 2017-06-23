import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
#yamite
import parser

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

def execute_task_dict(task_dict, driver):
    for task in task_dict:
        execute_task(task_dict, task, driver)

def execute_task(task_dict, task, driver):
    operation_list = task_dict[task]
    execute_operation_list(operation_list, driver)

def execute_operation_list(operation_list, driver):
    for operation_dict in operation_list:
        for operation_type, value in operation_dict.iteritems():
            element = run_operation_on_driver(operation_type, value, driver)
        time.sleep(1)

def run_operation_on_driver(operation_type, value, driver):
    element = None
    if operation_type == '$link':
        driver.get(value)
    elif operation_type == 'class':
        element = driver.find_element_by_class_name(value).click()
    elif operation_type == 'id':
        element = driver.find_element_by_id(value).click()
    elif operation_type == 'text_value':
        element = driver.find_element_by_xpath("//*[contains(text(), '" + value + "')] | //*[@value='" + value + "']").click()
        #driver.find_element_by_xpath("//*[contains(text(), 'Features')]").click()
        #driver.find_element_by_xpath("//*[contains(text(), '"+value+"')]").click()
    elif operation_type == '$type':
        actions.send_keys(value)
        actions.perform()

    else:
        print 'not built yet lmao'

    return element


#setup
driver = init_driver()
actions = ActionChains(driver)

parsed_yaml = parser.open_yaml("test.yaml")
task_dict = parser.create_task_dict(parsed_yaml)
execute_task_dict(task_dict, driver)

time.sleep(15)
driver.quit()





