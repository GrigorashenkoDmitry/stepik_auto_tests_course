import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("abc@abc.com")

    current_dir = os.path.abspath(os.path.dirname('__file__'))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()