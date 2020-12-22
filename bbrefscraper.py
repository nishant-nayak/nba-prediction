"""
            UNSTABLE!!! 
            
            DO NOT USE!!
"""

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

PATH="C:\\Program Files (x86)\\chromedriver.exe"
driver=webdriver.Chrome(PATH)
n_seasons=10
loc='D:\\Pranav\\Code\\IEEE\\bbref\\'

url="https://www.basketball-reference.com/leagues/NBA_2020_games.html"
driver.get(url)

def scrape(season,month):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
    except:
        print("did not scrape",season,month) 
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
    data.to_csv(loc+'\\'+season+month+".csv",header=True,index=True)

def seasonscrape(season):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "filter"))
        )     
        fil=driver.find_element_by_class_name("filter")
        months=[cell.text for cell in fil.find_elements_by_tag_name("div")]
        for month in months:
            try:
                link=WebDriverWait(driver,10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT,month))
                )
            except:
                print("skipped",month)
                continue
            link.click()
            scrape(season,month)
            driver.back()
    except: print("did not scrape",season)

while n_seasons>0 :
    try:
        title=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="meta"]/div[2]/h1/span[1]'))
        )
        os.mkdir(loc+title.text)
        seasonscrape(title.text)
    except: print("no data",n_seasons)
    n_seasons-=1
    try:
        link=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="meta"]/div[2]/div/a[1]'))
        )
        link.click()
    except: print("did not click",n_seasons)
driver.quit()