import pandas as pd

churn = pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Bank%20Churn%20Modelling.csv')

churn.head()

churn.tail()

churn.info()

churn.describe()

churn.columns

y = churn['Churn']
x = churn[['CreditScore', 'Geography', 'Gender', 'Age',
       'Tenure', 'Balance', 'Num Of Products', 'Has Credit Card',
       'Is Active Member', 'Estimated Salary']]

x.replace({'Geography':{'France':0,'Spain':1,'Germany':2}},inplace=True)
x.replace({'Gender':{'Male':0,'Female':1}},inplace=True)

from sklearn.model_selection import train_test_split

x_train , x_test ,y_train ,y_test = train_test_split(x,y,random_state=2529)

x_train.shape , x_test.shape ,y_train.shape ,y_test.shape

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=2000)

model.fit(x_train , y_train)

y_predict = model.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test , y_predict)
