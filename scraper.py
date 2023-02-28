from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os
import pickle
from datetime import datetime

options = Options()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait = WebDriverWait(driver, 20)

os.system("cls")

def clickElement(xpath):
    try:
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        element = driver.find_element_by_xpath(xpath)
        element.click()
    except Exception:
        print("\nCould not click element\n")

def locateElement(xpath):
    try:
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        element = element[0].get_attribute('innerHTML')
        element = BeautifulSoup(element, features="lxml")
        element = element.text
        return element
    except Exception: 
        print("\nCould not locate element\n")
        return ""

def send_keysElement(xpath, keys):
    try:
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        element = driver.find_element_by_xpath(xpath)
        element.send_keys(keys)
    except Exception:
        print("\nCould not send keys\n")

def run():
    driver.get('url here')
    clickElement('full xpath here')    

if __name__ == '__main__':
    run()


