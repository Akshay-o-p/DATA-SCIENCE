import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.svm import SVC

data=pd.read_csv('iris.csv')
print(data.head())

x=data.iloc[:,:-4]
print(x)

y=data.iloc[:,-1]
print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)

classifier=SVC(kernel='linear')
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)

print(y_pred)

cm=confusion_matrix(y_test,y_pred)
print(cm)

ac=accuracy_score(y_test,y_pred)
print(ac)
