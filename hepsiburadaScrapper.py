from cgitb import text
import click
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook, load_workbook


wb = Workbook()
ws=wb.active
ws.title= "Data"
input1 = input()
ArrayList =[]
PATH = "<Path_To_ChromeDriver>"
driver = webdriver.Chrome(PATH) 
driver.get("https://www.hepsiburada.com/")


def Yazdırma(a,b,c):
    ws.append([a]+[b]+[c])

driver.implicitly_wait(7)
searchbar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "SearchBoxOld-cHxjyU99nxdIaAbGyX7F")
        )
)
a = driver.find_element(By.CLASS_NAME, "desktopOldAutosuggestTheme-UyU36RyhCTcuRs_sXL9b")
a.send_keys(input1)
searchbar.click()
time.sleep(8)
articles=driver.find_elements(By.CSS_SELECTOR,"[data-test-id=product-card-name")
price=driver.find_elements(By.CSS_SELECTOR,"[data-test-id='price-current-price")
for value,value2, in zip(articles,price):

    c = value.text
    d = value2.text
    target = driver.find_element(By.XPATH,"//a[@title='{0}']".format(c)).get_attribute("href")
    Yazdırma(c,d,target)

wb.save('Save_OPath')
