import preprocessing as pp
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Creating and trainning our model
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
mlp.fit(pp.X_train, pp.y_train)

# Predict
predicted = mlp.predict(pp.X_test)

print(accuracy_score(pp.y_test, predicted))
print(confusion_matrix(pp.y_test,predicted))
print(classification_report(pp.y_test,predicted))