# -*- coding: utf-8 -*-
"""ybi servo prediction(final project)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QB2rwS0erTBnTsi4vXtLF7XFQCtMypEe

**Importing Library**
"""

import pandas as pd

import numpy as np

"""**Importing CSV as DataFrame**"""

df = pd.read_csv(r'https://github.com/YBI-Foundation/Dataset/raw/main/Servo%20Mechanism.csv')

"""**Getting the First Five rows of DataFrame**"""

df.head()

"""**Getting Information of DataFrame**"""

df.info()

"""**Getting** **the** **Summary** **Statistics**"""

df.describe()

"""**Getting Column names**"""

df.columns

"""**Getting shape of Dataframe**"""

df.shape

"""**Getting Categories and Counts of Categorical Variables**"""

df[['Motor']].value_counts()

df[['Screw']].value_counts()

df.replace({'Motor':{'A':0,'B':1,'C':2,'D':3,'E':4}},inplace=True)

df.replace({'Screw':{'A':0,'B':1,'C':2,'D':3,'E':4}},inplace=True)

"""**Defining Y and X variables**"""

y=df['Class']

y.shape

y

X=df[['Motor','Screw','Pgain','Vgain']]

X=df.drop('Class',axis=1)

X.shape

X

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.3,random_state=2529)

X_train.shape,X_test.shape,Y_train.shape,Y_test.shape

"""**Getting Model Train**"""

from sklearn.linear_model import LinearRegression

lr=LinearRegression()

lr.fit(X_train,Y_train)

"""**Getting Model Prediction**"""

y_pred = lr.predict(X_test)

y_pred.shape

y_pred

"""**Getting Model Evaluation**"""

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

mean_squared_error(Y_test,y_pred)

mean_absolute_error(Y_test,y_pred)

r2_score(Y_test,y_pred)

"""**Getting Visualization of Actual Vs Predicted Results**"""

import matplotlib.pyplot as plt
plt.scatter(Y_test,y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")
plt.show()

"""**Getting Future Predictions**"""

X_new =df.sample(1)

X_new=df.sample(1)

X_new

X_new.shape

X_new=X_new.drop('Class',axis=1)

X_new

X_new.shape

y_pred_new=lr.predict(X_new)

y_pred_new

