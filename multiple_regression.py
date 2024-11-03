from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.datasets import load_iris

data =load_iris()
x=data.data
y=data.target

x_train, x_test, y_train, y_test=train_test_split(x,y,random_state=42)

classifier=LinearRegression()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
y_predict_train=classifier.predict(x_train)
r2=r2_score(y_test,y_pred)
ms=mean_squared_error(y_test,y_pred)
print(r2)
print(ms)