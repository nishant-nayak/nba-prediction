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

url="https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2019-20&SeasonType=Regular%20Season&Month=1"
driver.get(url)
time.sleep(5)
button=driver.find_element_by_id("onetrust-accept-btn-handler")
button.click()
loc='D:\\Pranav\\Code\\IEEE\\nbastats\\'
n_seasons=10


def monthscrape(season,month):
    print("at",month)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
    except:
        print("did not scrape",month)
        return
    table=driver.find_elements_by_tag_name('table')[0]
    df=[[cell.text for cell in row.find_elements_by_tag_name('td')] for row in table.find_elements_by_tag_name('tr')]
    del df[0]
    col=table.find_element_by_tag_name('thead')
    headings=[title.text for title in col.find_elements_by_tag_name('th')]
    while headings[-1]=='': headings.pop()
    data=pd.DataFrame(df,columns=headings)
    print("dataframe made")
    data.to_csv(loc+season+'\\'+month+'.csv',header=True,index=False)


def seasonscrape(season):
    print("at",season)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/label/select/optgroup[2]"))
        )
    except :
        print("did not find filter")
        return
    fil=driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/label/select")
    options=fil.find_elements_by_tag_name('optgroup')[1]
    for option in options.find_elements_by_tag_name('option'):
        try:
            element=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/label/select"))
            )
            element.click()
            option.click()
            driver.implicitly_wait(3)
            monthscrape(season,option.text)
        except:
            print("could not click",season,option.text)

#__main__
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/main/div/div/div[2]/div/div/div[1]/div[1]/div/div/label/select"))
    )
    seasonfilter=driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/div[1]/div[1]/div/div/label/select')
    for season in seasonfilter.find_elements_by_tag_name('option'):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/main/div/div/div[2]/div/div/div[1]/div[1]/div/div/label/select"))
            )
            seasonfilter.click()
            driver.implicitly_wait(3)
            season.click()
            seasonscrape(season.text)
        except:
            print("could not scrape",season.text)
        n_seasons-=1
        if(n_seasons==0) : break 
except:
    print("not found")
driver.quit()