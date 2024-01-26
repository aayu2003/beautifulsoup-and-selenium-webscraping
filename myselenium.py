from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time
chrome_driver_path = r"C:\Program Files (x86)\chromedriver.exe"

chrome_service=ChromeService(chrome_driver_path)
chrome_option=webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_option)

driver.get('https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm')

input_element = driver.find_element('name','htf')
input_element.send_keys("5")
input_element1 = driver.find_element('name','hti')
input_element1.send_keys("11")
input_element2 = driver.find_element('name','wt')
input_element2.send_keys("100")

button_element=driver.find_element('id','calcbmi')
button_element.click()
time.sleep(1)
output=driver.find_element('name','bmi')
print(output.get_attribute('value'))
time.sleep(5)
driver.quit()