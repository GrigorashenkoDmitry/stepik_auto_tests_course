from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc (x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:

	browser = webdriver.Chrome()
	browser.implicitly_wait(12)

	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	element = browser.find_element_by_id("price")

	element = WebDriverWait(browser,12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "$100")
	)

	button = browser.find_element_by_id("book")
	button.click()

	x = browser.find_element_by_id("input_value").text

	input = browser.find_element_by_id("answer")
	input.send_keys(calc(x))

	button = browser.find_element_by_id("solve")
	button.click()

finally:
	time.sleep(10)
	browser.quit()