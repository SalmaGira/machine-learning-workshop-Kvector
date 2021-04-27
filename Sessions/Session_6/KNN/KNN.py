from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

#Load dataset
wine = datasets.load_wine()

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3) # 70% training and 30% test

#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=7)

#Train the model using the training sets
knn.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)

scores = {}
scores_list = []

krange = range(1,26)
for k in krange:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    ypred = knn.predict(X_test)
    scores[k] = metrics.accuracy_score(y_test, ypred)
    scores_list.append(scores[k])

plt.plot(krange, scores_list)
plt.xlabel('Values of K for KNN')
plt.ylabel('Testing Accuracy')
plt.show()
