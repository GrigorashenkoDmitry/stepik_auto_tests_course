from selenium import webdriver
import time

try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_id("num1").text

    b = browser.find_element_by_id("num2").text

    c = sum = (int(a)+int(b))
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(value=str(c))

    button = browser.find_element_by_class_name("btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()