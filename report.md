# NBA Data Analysis

**Introduction**

The National Basketball Association (NBA) is vastly considered to be the premier men’s basketball league in the world and is watched by millions of viewers every season. From the moment the jump ball is tossed at the beginning of each game, the question on everyone’s mind is “who will the winner be?”. Most NBA commentators and betting sites make fairly accurate predictions on the outcome of the game. The objective of this project is to build our very own “expert” to do the same using machine learning.

**Brief Overview**

The most basic model that we implemented considered a team to be an atomic unit. This meant that the data used to train the model was a team’s statistics instead of the players that constituted it. The outcomes predicted by this model were right about 70% of the time which is on par with most betting sites and expert opinions. Also, given that these games generally have an upset rate of ~30% it seems that our model was doing the best it could. 

This however has an obvious flaw. Teams are often reformed each season and the statistics for the past season may no longer be reliable. To address this issue, we considered building a model using more nuanced data i.e. the player information. Our approach was to quantify the synergy between players on the same team as well as the dominance they assert over their adversary. In fact, we learnt that player identity alone is sufficient to calculate these quantities and make fairly accurate predictions.

Although up till this point our models were geared to predicting the game outcome, we now turned our attention to predicting more short term events which occur during the course of the game. Turnovers, steals and rebounds (both offensive and defensive) are examples of such events. To do so, our data had to be even more detailed which is why we looked at the box scores of a game. Box scores contain information of not only each event, but also on the players who were present on the court when that event occured. This data, combined with probit regression models, led us to understand that we can make predictions not only on the outcome of the game, but also on events that occur in it.

Finally we looked at a model to build a team that has the best chance at beating a given opponent. This is similar to how teams are formed in Fantasy Basketball leagues. Here we understood how the data was scraped, cleaned and merged and how its features were explored. We observed the performance of some base models and then with a Bayesian optimisation method, found the best parameters for a boosting model using lightGBM. We also looked at three different neural network architectures and noticed that, while deep learning models might not suit this dataset of limited size, it shows improvement compared to boosting models.

### Results of games

... Nishant

#### Box Score

... Nishant

### Synergy

... Sanjkeet

### Positive and Negative Synergies

...Harsh

### Generating Line ups

...

Light Sanjkeet, Harsh

**Neural Networks**

In order to understand the insight that deep learning can give to this task, we observed 3 different neural networks. All of them were built using TensorFlow 2 with a Keras backend. Each of the models used the ReLU activation function in hidden layers, root mean square error for the loss function and the Adam optimizer. All of them were trained for 100 epochs.

Model 1 consisted of 4 layers, with 64 and 32 units in the first and second hidden layers respectively. From the plot of training and cross validation errors, we can see that the model starts overfitting the data after the first few epoch since there is a significant difference in training and cross validation error which only increases as the training progresses.

![Training and Cross validation error plot for model 1](/images/model1plot.png)

Model 2 consisted of 5 layers, with 64, 128 and 32 units in the hidden layers. Dropout regularization was implemented between the fourth and output layer as well. This model performed the best among the 3 since it did not overfit the data to a large extent and had fairly small differences in the train and cross validation errors.

![Training and Cross validation error plot for model 2](/images/model2plot.png)

Model 3 also consisted of 5 layers but had 128,256 and 64 units in the hidden layers. Once again we added dropout regularization between the fourth and output layers. This model performed worse than model 2. Although increasing the number of units in the hidden layers often allows the model to learn more complex functions, in this case, the density of connections actually led to overfitting. We can observe this in the graph as well since the difference between the cross validation and train error increases consistently after ~40 epochs.

![Training and Cross validation error plot for model 3](/images/model3plot.png)

We can conclude that although deep learning might not be best suited for this task due to the limited size of the dataset, it does provide a slight improvement compared to the boosting models.

GA Prajna

### Expert Opinion

... Prajna