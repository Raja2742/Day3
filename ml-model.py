import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('iris.csv')
print(df.head())
from sklearn.model_selection import train_test_split
x=df.drop('species',axis=1)
y=df['species']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print(x)
print(y)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
dt_model=DecisionTreeClassifier()
dt_model.fit(x_train,y_train)
y_predict_dt=dt_model.predict(x_test)
acc_dl=accuracy_score(y_test,y_predict_dt)
print(acc_dl)
print(f"decision tree accuracy score is {acc_dl*100:.2f}%")
from sklearn.linear_model import LogisticRegression
l_model=LogisticRegression()
l_model.fit(x_train,y_train)
y_predict_l=l_model.predict(x_test)
acc_l=accuracy_score(y_test,y_predict_l)
print(acc_l)
print(f"logistic regression accuracy score is {acc_l*100:.2f}%")
results=pd.DataFrame({
    'model':["decision tree","logistic regression"],
    'accuracy score':[acc_dl,acc_l]
    })
print(results)
sns.barplot(x='model',y='accuracy score',data=results)
plt.show()