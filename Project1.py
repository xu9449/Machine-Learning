import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

with open ("diabetes.csv", 'r') as csvfile:
 diab = pd.read_csv(csvfile)
print(diab.head())

X = diab.drop('Outcome', axis=1).values
y = diab['Outcome'].values

from sklearn.model_selection import train_test_split
X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.4, random_state=42, stratify=y)

# import KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier

# Setup arrays to store training and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

for i, k in enumerate(neighbors):
    # Setup a knn classifier with k neighbors
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the model
    knn.fit(X_train, y_train)

    # Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    # Compute accuracy on the test set
    test_accuracy[i] = knn.score(X_test, y_test)

    plt.title('k-NN Varying number of neighbors')
    plt.plot(neighbors, test_accuracy, label='Testing Accuracy')
    plt.plot(neighbors, train_accuracy, label='Training accuracy')
    plt.xlabel('Number of neighbors')
    plt.ylabel('Accuracy')
    plt.show()

    knn = KNeighborsClassifier(n_neighbors= 7)
    knn.fit(X_train, y_train)
    # KNeighborsClassifier(algorithm='auto', leaf_size=30)
    knn.score(X_test,y_test)
    print(knn.score(X_test,y_test))

    from sklearn.metrics import confusion_matrix
    y_pred = knn.predict(X_test)
    print(confusion_matrix(y_test,y_pred))
    print(pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True))

    from sklearn.metrics import classification_report
    print(classification_report(y_test, y_pred))

    y_pred_proba = knn.predict_proba(X_test)[:, 1]
    from sklearn.metrics import roc_curve
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.plot(fpr, tpr, label='Knn')
    plt.xlabel('fpr')
    plt.ylabel('tpr')
    plt.title('Knn(n_neighbors=7) ROC curve')
    plt.show()

    from sklearn.metrics import roc_auc_score
    roc_auc_score(y_test, y_pred_proba)

    from sklearn.model_selection import GridSearchCV
    param_grid = {'n_neighbors': np.arange(1,50)}
    knn = KNeighborsClassifier()
    knn_cv = GridSearchCV(knn, param_grid, cv = 5)
    knn_cv.fit(X,y)

    print(knn_cv.best_score_)
    print(knn_cv.best_params_)