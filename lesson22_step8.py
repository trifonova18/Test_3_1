import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/file_input.html')
driver.maximize_window()

first_name = driver.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
first_name.send_keys('Anna')

last_name = driver.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
last_name.send_keys('Ivanova')

email = driver.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
email.send_keys('abc@yandex.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
button = driver.find_element(By.XPATH, '//*[@id="file"]')
button.send_keys(file_path)

submit = driver.find_element(By.XPATH, '/html/body/div/form/button')
submit.click()


time.sleep(10)
driver.quit()