# nba-predictions

A project to predict the outcome of NBA matches using Machine Learning.

## Data Description

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

## Directory Description

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


## Resources 

nbastats - https://www.nba.com/stats/teams/traditional/?sort=W_PCT&dir=-1&Season=2019-20&SeasonType=Regular%20Season&Month=1

bbref - https://www.basketball-reference.com/leagues/NBA_2020_games.html

pilot - https://towardsdatascience.com/building-my-first-machine-learning-model-nba-prediction-algorithm-dee5c5bc4cc1

scraping data - https://www.youtube.com/playlist?list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ

all nba team prediction model - https://www.kaggle.com/felixdonovan/predicting-the-all-nba-teams

nba all star league prediction model - https://towardsdatascience.com/using-machine-learning-to-predict-nba-all-stars-part-2-modelling-a66e6b534998

evaluating player similarity - https://towardsdatascience.com/which-nba-players-are-most-similar-machine-learning-provides-the-answers-r-project-b903f9b2fe1f

player ranking in soccer - https://arxiv.org/pdf/1802.04987.pdf

predict strategy of a team - https://www.mdpi.com/2076-3417/10/1/24/htm

selecting a team to beat a given opponent - https://thesai.org/Downloads/Volume8No8/Paper_59-Automated_Player_Selection_for_a_Sports_Team.pdf

use individual player stats to come up with the team stats and use the pilot model to predict the winner?


