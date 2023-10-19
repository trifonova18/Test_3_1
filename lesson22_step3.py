import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://suninjuly.github.io/selects1.html')
driver.maximize_window()

num1 = driver.find_element(By.XPATH, '//*[@id="num1"]')
num1 = num1.text

num2 = driver.find_element(By.XPATH, '//*[@id="num2"]')
num2 = num2.text

y = int(num1) + int(num2)
y = str(y)

string = Select(driver.find_element(By.XPATH, '//*[@id="dropdown"]'))
string.select_by_visible_text(y)

button = driver.find_element(By.XPATH, '/html/body/div/form/button')
button.click()

time.sleep(5)
driver.quit()