import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.svm import SVR, SVC

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

class MachineLearning:

    def run_classification_methods(self):
        '''
        Perform machine learning on the csv file. Use the first 80% of the samples to train the model and the last 20% to test the model.
        Use the following algorithms: Logistic Regression, Random Forest, Support Vector Machine
        '''

        # Read the csv file
        df = pd.read_csv("samples.csv", header=None)
        # Split the data into features and labels
        gate_index = int(df.iat[0, 0])
        if gate_index == 0: # If the gate index is 0, then the gate is not included in the csv file and we need to use all the features
            X = df.iloc[:, 1:-1].values
            y = df.iloc[:, -1].values
        else:
            X = df.iloc[:, 1:gate_index].values 
            y = df.iloc[:, -1].values
            
        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        # Scale the data. This is necessary for SVM, because it uses the euclidean distance.
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        # Train the model
        models = []
        models.append(("LR", LogisticRegression()))
        models.append(("RF", RandomForestClassifier()))
        models.append(("SVM", SVC()))

        for name, model in models:
            model.fit(X_train, y_train)
            # Evaluate the model
            y_pred = model.predict(X_test)
            print(name, ":", metrics.classification_report(y_test, y_pred))
            
            # Calculate confusion matrix
            cm = confusion_matrix(y_test, y_pred)
            print(name, " Confusion Matrix:")
            print(cm)
            
            # Plot confusion matrix with labels "Acceptable", "Success", "Failure"
            sns.heatmap(cm, annot=True, fmt='g', xticklabels=["Acceptable", "Failure", "Sucess"], yticklabels=["Acceptable", "Failure", "Success"], cmap="Blues")
            plt.xlabel("Predicted")
            plt.ylabel("Actual")
            plt.title(name + " Confusion Matrix")
            plt.show()

            


    def run_regression_methods(self):
        '''
        Perform machine learning on the csv file. Use the first 80% of the samples to train the model and the last 20% to test the model.
        Use the following algorithms: Linear Regression, Random Forest, Support Vector Machine, Decision Tree
        '''
        # Read the csv file
        df = pd.read_csv("samples.csv", header=None)
        # Split the data into features and labels
        gate_index = int(df.iat[0, 0])
        if gate_index == 0: # If the gate index is 0, then the gate is not included in the csv file and we need to use all the features
            X = df.iloc[:, 1:-1].values
            y = df.iloc[:, -2].values
        else:
            X = df.iloc[:, 1:gate_index].values 
            y = df.iloc[:, -2].values

        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        # Scale the data. This is necessary for SVM, because it uses the euclidean distance.
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        # Train the model
        models = []
        models.append(("LR", LinearRegression()))
        models.append(("RF", RandomForestRegressor()))
        models.append(("SVM", SVR()))
        models.append(("DT", DecisionTreeRegressor()))

        for name, model in models:
            model.fit(X_train, y_train)
            # Evaluate the model
            y_pred = model.predict(X_test)
            print(name, ":", metrics.r2_score(y_test, y_pred))
            print(name, ":", metrics.mean_squared_error(y_test, y_pred))