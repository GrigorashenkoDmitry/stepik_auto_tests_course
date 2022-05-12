from selenium import webdriver
import time
import math

def calc (x):
	return str(math.log(abs(12*math.sin(int(x)))))
try:
	
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_css_selector("button")
	button.click()

	browser.switch_to.window(browser.window_handles[1])

	time.sleep(1)

	x = browser.find_element_by_id("input_value").text

	input = browser.find_element_by_id("answer")
	input.send_keys(calc(x))

	button = browser.find_element_by_class_name("btn.btn-primary")
	button.click()

finally:
	time.sleep(10)
	browser.quit()