import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

driver = webdriver.Chrome()
driver.get('https://suninjuly.github.io/execute_script.html')
driver.maximize_window()

x = driver.find_element(By.XPATH, '//*[@id="input_value"]')
x = x.text
y = str(math.log(abs(12*math.sin(int(x)))))

driver.execute_script('window.scrollBy(0, 100);')

answer = driver.find_element(By.XPATH, '//*[@id="answer"]')
answer.send_keys(y)

button_robot = driver.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
button_robot.click()

button_rule = driver.find_element(By.XPATH, '//*[@id="robotsRule"]')
button_rule.click()

submit = driver.find_element(By.XPATH, '/html/body/div/form/button')
submit.click()

time.sleep(5)
driver.quit()