#Logistic Regression Project 

#Import Libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Read th file 

ad_data = pd.read_csv('advertising.csv')

#Check the head of the data
ad_data.head()
#Output for this line of code can be viewed at: http://tinyurl.com/yauhb9h9

#Use info and describe() on ad_data

ad_data.info()
#Output for this line of code can be viewed at : http://tinyurl.com/yct5awfx
ad_data.describe()
#Output for this line of code can be viewed at : http://tinyurl.com/y7o2gv2l
#Exploratory Data Analysis
#Let's use seaborn to explore the data!
#Try recreating the plots shown below!
#Create a histogram of the Age

sns.set_style('whitegrid')
ad_data['Age'].hist(bins=30)
plt.xlabel('Age')

#Output for this line of code can be viewed at : http://tinyurl.com/yc324ekg

#Create a jointplot showing are income versus Age
sns.jointplot(x='Age',y='Area Income',data=ad_data)
#Output fo this line of code can be viewed at : http://tinyurl.com/y8ulf3dd

#Create a jointplot showing the kde distributrions of Daily Time Spent on Site Vs Age 
sns.jointplot(x='Age',y='Daily Time Spent on Site',data=ad_data,color='red',kind='kde')
#Output for this line f code can be viewed at : http://tinyurl.com/yctt6q6r
#Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage'

sns.jointplot(x='Daily Time Spent on Site',y='Daily Internet Usage',data=ad_data,color='green')
#Output for this line of code can be viewed at : http://tinyurl.com/y8pud54z

#Finally, create a pairplot with the hue defined by the 'Clicked on Ad' column feature.

sns.pairplot(ad_data,hue='Clicked on Ad',palette='bwr')
#Output for this line of code an be viewed at : http://tinyurl.com/y7fps9qp

#Logistic Regression

#Now it's time to do a train test split, and train our model!

#Split the data into training set and testing set using train_test_split

from sklearn.model_selection import train_test_split

X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']]

y = ad_data['Clicked on Ad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#Train and fit a logistic regression model on the training set.

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()

logmodel.fit(X_train,y_train)


#Predictions and Evaluations

#Now predict values for the testing data.

predictions = logmodel.predict(X_test)
 
#Create a classification report for the model.

from sklearn.metrics import classification_report

print(classification_report(y_test,predictions))
#Output for this line of code an be viewed at : http://tinyurl.com/y84rhuqn


