import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

PATH="C:\\Program Files (x86)\\chromedriver.exe"
driver=webdriver.Chrome(PATH)

url="https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=1996-97&SeasonType=Regular%20Season&Month=4"
driver.get(url)
button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'onetrust-accept-btn-handler'))
)
button.click()
loc=r'D:\\Pranav\\Code\\IEEE\\nbastats\\crossvalidation\\'

def scrape(month):
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
    data.to_csv(loc+month+'.csv',header=True,index=False)       


try:
    fil = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/label/select"))
    )
    print(fil.text)
    options=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/label/select/optgroup[2]'))
    )
    print(options.text)
    for option in options.find_elements_by_tag_name('option'):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/label/select"))
            )
            element.click()
            option.click()
            time.sleep(5)
            scrape(option.text)
        except:
            print("could not click",option.text)
except:
    print("not found")
    driver.quit()
driver.quit()