import math
import random
import matplotlib
import preprocessing as pp
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# We're going to use k = sqrt(n), 'n' num of rows in train set
k = int(round(math.sqrt(len(pp.df.index)))) # faster than df.shape[0]

# Creating our model
model = KNeighborsClassifier(n_neighbors=k)

# Training the model using training set
model.fit(pp.X_train,pp.y_train)

# Predict
predicted = model.predict(pp.X_test)

print(accuracy_score(pp.y_test, predicted))
print(confusion_matrix(pp.y_test,predicted))
print(classification_report(pp.y_test,predicted))