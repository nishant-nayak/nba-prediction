# nba-predictions

A project to predict the outcome of NBA matches using Machine Learning.

# Data Description

Note that the columns with column names as Team1COLNAME and Team2COLNAME correspond to the same COLNAME description, and the two columns refer to the two teams playing that game. Also, note that the statistics were taken on a month-wise basis from [Basketball Reference](https://www.basketball-reference.com/) and the [official NBA Website](https://www.nba.com/stats/).

| Column Name |                         Description                         |
|:-----------:|:-----------------------------------------------------------:|
|     AWAY    | The Away team, this team is not playing on their home court |
|     Pts     |            The number of points scored by a team            |
|     HOME    |   The Home team, this team is playing on their home court   |
|     RANK    |              The month-wise ranking of the team             |
|      GP     |                    Number of Games Played                   |
|      W      |                        Number of Wins                       |
|      L      |                       Number of Losses                      |
|     MIN     |                   Number of Minutes Played                  |
|    OFFRTG   |                       Offensive Rating                      |
|    DEFRTG   |                       Defensive Rating                      |
|    NETRTG   |                          Net Rating                         |
|     AST%    |                      Assist Percentage                      |
|    AST/TO   |                   Assist to Turnover Ratio                  |
|  AST_RATIO  |                         Assist Ratio                        |
|    OREB%    |                 Offensive Rebound Percentage                |
|    DREB%    |                 Defensive Rebound Percentage                |
|     REB%    |                      Rebound Percentage                     |
|     TOV%    |                     Turnover Percentage                     |
|     EFG%    |               Effective Field Goal Percentage               |
|     TS%     |                   True Shooting Percentage                  |
|     PACE    |                             Pace                            |
|     PIE     |                    Player Impact Estimate                   |

# Directory Description

### [/datasets](/datasets/)
Contains all the raw and preprocessed datasets.

### [/webdriver](/webdriver/)
Contains the Chrome webdriver used for data scraping.

### [data_scraping.py](/data_scraping.py)
Python File to scrape the relevant data from the internet.

### [data_preprocessing.ipynb](/data_preprocessing.ipynb)
Jupyter Notebook used for data preprocessing.

### [data_modelling.ipynb](/data_modelling.ipynb)
Jupyter Notebook used to fit simple Machine Learning models to the data.

