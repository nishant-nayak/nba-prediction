import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


PATH="C:\\Program Files (x86)\\chromedriver.exe"
driver=webdriver.Chrome(PATH)
loc=r'D:\\Pranav\\Code\\IEEE\\bbref\\crossvalidation\\'

url="https://www.basketball-reference.com/leagues/NBA_1997_games.html"
driver.get(url)

def scrape(month):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
    except: 
        return
    table=driver.find_elements_by_tag_name('table')[-1]
    df,headings,skip=[],[],1
    for row in table.find_elements_by_tag_name('tr'):
        if skip :
            headings=[cell.text for cell in row.find_elements_by_tag_name('th')]
            skip=0
            continue
        head=row.find_element_by_tag_name('th').text
        df.append([head]+[cell.text for cell in row.find_elements_by_tag_name('td')])
    data=pd.DataFrame(df,columns=headings)
    data.to_csv(loc+month+".csv",header=True,index=True)


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "filter"))
    )
    fil=driver.find_element_by_class_name("filter")
    months=[cell.text for cell in fil.find_elements_by_tag_name("div")]
    print(months)
    for month in months:
        try:
            link=WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.LINK_TEXT,month))
            )
        except:
            print("skipped",month)
            continue
        link.click()
        print(month)
        scrape(month)
        driver.back()
except:
    driver.quit()
driver.quit()