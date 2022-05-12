from selenium import webdriver
import time
import math

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))
try:

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_class_name("btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:

    time.sleep(10)
    browser.quit()
