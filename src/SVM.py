import pandas as pd
from sklearn import metrics
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix

dataset=pd.read_csv('dataset.csv',names=['curr_derivative','mean','label'])
y=dataset.label
x=dataset.drop('label',axis=1)
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

#svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Training the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Model Precision: what percentage of positive tuples are labeled as such?
print("Precision:",metrics.precision_score(y_test, y_pred))

# Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, y_pred))

print('Confusion matrix is as follows\n',confusion_matrix(y_test,y_pred))
print('Accuracy Metrics')
print(classification_report(y_test,y_pred))
print(" correct predicition",metrics.accuracy_score(y_test,y_pred))
print(" worng predicition",(1-metrics.accuracy_score(y_test,y_pred)))

