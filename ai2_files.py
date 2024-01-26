from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import os
import time
chrome_driver_path = r"C:\Program Files (x86)\chromedriver.exe"

chrome_service=ChromeService(chrome_driver_path)
chrome_option=webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_option)

driver.get('https://smallpdf.com/word-to-pdf#r=convert-to-word')

main_window_handle = driver.current_window_handle

button_element = driver.find_element(By.CLASS_NAME, 'l3tlg0-0.ggoliT')
button_element.click()


 
file_input = driver.find_element('id','__picker-input')
file_path = os.path.abspath(r'C:\Users\aa738\Downloads\Issues.docx')
file_input.send_keys(file_path)

time.sleep(10)