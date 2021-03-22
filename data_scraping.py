from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

# Path to the working directory
PATH = os.path.dirname(__file__)

# Year from which data should start being collected, 2019 refers to the 2018-19 season
START_YEAR = 2019

# Year till which data should be collected, 2019 refers to the 2018-19 season
END_YEAR = 2019

# Excluding months May and June since the NBA Website does not have stats for those months
months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']

# Initializing the web driver, downloaded from https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome(executable_path = PATH + '/webdriver/chromedriver.exe')

for year in reversed(range(START_YEAR, END_YEAR+1)):
    
    # Initializing the final dataframe
    df_final = pd.DataFrame()

    # Using index to loop through list since the NBA Website URLs takes month in form of a number
    for j in range(len(months)):

        # Initialize temporary lists to store monthly data
        result = []
        stat = []

        # Get website for matchwise results
        driver.get("https://www.basketball-reference.com/leagues/NBA_"+str(year)+"_games-"+months[j]+".html")

        # Waiting until the page loads to proceed
        table_1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "schedule"))
        )

        # Calculating the number of rows and columns in the table
        rows = len(table_1.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr"))
        cols = len(table_1.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/div[2]/div/table/thead/tr').find_elements_by_tag_name("th"))

        # Starting loop from 1 since XPath indexing starts from 1
        for r in range(1, rows+1):

            # After every 25 rows, the headings repeat and we do not require this in our dataset, so we check and continue
            if driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr['+str(r)+']').get_attribute('class') == 'thead':
                continue
            
            # Initializing a temporary list to store row-wise data
            temp = []
            
            # Appending the date first, followed by the team names and scores
            temp.append(driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr['+str(r)+']/th').text)
            for c in range(2, cols-4):
                temp.append(driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr['+str(r)+']/td['+str(c)+']').text)

            # Append row-wise results to the monthly result list
            result.append(temp)


        # Get website for monthwise statistics
        driver.get('https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=' + str(year-1) + '-' + str('{:02d}'.format(year%100)) + '&SeasonType=Regular%20Season&Month=' + str(j+1))
        
        # Waiting until the page loads to proceed
        table_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "nba-stat-table__overflow"))
        )

        # Calculating the number of rows and columns in the table
        rows = len(table_2.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr'))
        cols = len(driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr[1]').find_elements_by_tag_name('td'))

        for r in range(1, rows+1):
            
            # Creating a temporary list to store row-wise data
            temp = []

            for c in range(1, cols+1):
                data = driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr['+str(r)+']/td['+str(c)+']').text
                
                # NBA Website stores Los Angeles Clippers as LA Clippers, but the results website stores it as Los Angeles Clippers. Normalizing this convention in order to merge datasets later.
                temp.append(data if data != "LA Clippers" else 'Los Angeles Clippers')

            # Append row-wise stats to the monthly stats list
            stat.append(temp)

        # Creating Pandas DataFrames in order to merge the two datasets
        df_result = pd.DataFrame(result)
        df_stat = pd.DataFrame(stat)

        # Assigning column names to the datasets
        df_result.columns = ['Date', 'Team1AWAY', 'Team1Pts', 'Team2HOME', 'Team2Pts']
        df_stat.columns = ['RANK', 'TEAM', 'GP', 'W','L', 'MIN', 'OFFRTG', 'DEFRTG', 'NETRTG', 'AST%', 'AST/TO','AST_RATIO','OREB%','DREB%','REB%','TOV%','EFG%','TS%','PACE','PIE']
        
        # Merging the two datasets using team names
        df_temp = df_result.merge(df_stat.add_prefix('Team1'), how='left', left_on=['Team1AWAY'], right_on=['Team1TEAM']).drop(['Team1TEAM'], 
            axis=1).merge(df_stat.add_prefix('Team2'), how='left', left_on=['Team2HOME'], right_on=['Team2TEAM']).drop(['Team2TEAM'], axis=1)

        # Appending the monthly results to the final dataframe
        df_final = df_final.append(df_temp)

    # Exporting the yearly data into a .csv file without an index column
    df_final.to_csv(PATH + '/datasets/' + str(year) + '.csv', index=False)
    print("Finished " + str(year) + "!")

# Closing the driver after completion of scraping all the required data
print("\nFinished scraping all data!")
driver.close()