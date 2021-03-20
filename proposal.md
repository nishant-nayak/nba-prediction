# NBA Data Analysis

.... Pranav

## Results of games

Each game in a season of NBA is associated with many stats. These stats range from the number of points scored by each team in the game, to the percentage of baskets that were a result of a player's assist. These statistics can be used to help a machine learning program *learn* how a particular team will perform against another team.

Performing web scraping on popular basketball statistics websites like [Basketball-Reference.com](https://www.basketball-reference.com/) and the official [NBA Stats Website](https://www.nba.com/stats/), we were able to extract the month-wise stats for each team that played a game in the regular NBA Season of 2018-19. On performing Exploratory Data Analysis, we were able to find highly correlated features which would have an undesired effect on the learning of the machine learning model. The following heatmap shows the correlation coefficients of some of the input features:

![heatmap-image](/assets/heatmap.png)

After fitting the model on the preprocessed data using several different machine learning model architectures, we were able to obtain a model that was able to successfully predict the outcome of NBA games with **~73% accuracy**.

![training-img](/assets/train.png)

## Box Score

In basketball, box scores provide detailed statistics about each **player** who is on the lineup for a game. Additionally, it contains some team-level information like the 5 players who started the game, team rebounds, etc.
These box scores provide valuable insights on the skills of each player, and allows a machine learning model to learn certain performance metrics about each player and predict a player's performance in a simulated scenario.

Box scores only provide advanced statistics for plays that occur on the basketball court, during the game. However, other features which might not be related to the actual basketball game may be of importance to predict a player's (and the whole team's) performance. Some examples may include the number of rest days between two games, the geographical distance travelled by the team between two games, etc. *"Clutch"* moments in a game (game situations which are more important than others) are also a major consideration when evaluating a player's performance at a particular time in the game.

Using feature selection algorithms and Support Vector Machines (SVM) to predict the performance of team-level and player-level performances, the results prove to be **~2-3% more accurate** than publicly available state-of-the-art predictors of NBA game outcomes.

## Synergy

... Sanjkeet

## Positive and Negative Synergies

... Harsh

## Generating Line ups

...

Light Sanjkeet, Harsh

NN Pranav

GA Prajna

## Expert Opinion

... Prajna
