import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(url)

browser.find_element(By.CSS_SELECTOR, "button").click()
alert = browser.switch_to.alert
alert.accept()

x = int(browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value").text)
result = str(math.log(abs(12*math.sin(x))))
browser.find_element(By.ID, "answer").send_keys(result)
browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
time.sleep(3)

browser.quit()

