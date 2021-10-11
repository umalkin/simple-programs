import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

data = pd.read_csv('titanic.csv')

data.drop(['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)

y = pd.DataFrame(data['Survived'])
X = pd.DataFrame(data.drop(['Survived'], axis=1))

X = pd.get_dummies(X)
y = np.array(np.array(y).transpose()[0])

X['Age'].fillna(np.round(np.mean(X['Age'])), inplace=True)
X['Fare'].fillna(np.round(np.mean(X['Fare'])), inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=5)
lg = LogisticRegression(solver='lbfgs')
svc = SVC(gamma=0.05)

knn.fit(X_train, y_train)
lg.fit(X_train, y_train)
svc.fit(X_train, y_train)

hula = knn.predict(X_test)
hula1 = lg.predict(X_test)
hula2 = svc.predict(X_test)

print('KNN Accuracy rate -  %i percent' % (knn.score(X_test, y_test)* 100)) # 75
print('LogReg Accuracy rate -  %i percent' % (lg.score(X_test, y_test)* 100)) # 89
print('SVM SVC Accuracy rate -  %i percent' % (svc.score(X_test, y_test)* 100)) # 75 - gamma=auto, 79 - gamma=scale, 80 - gamma=0.05
