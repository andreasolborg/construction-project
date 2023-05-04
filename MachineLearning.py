"""
Author: Andreas Olborg and Jon Grendstad
Group: group 4
"""

import numpy as np
import pandas as pd
from sklearn import metrics, svm
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns, matplotlib.pyplot as plt

class MachineLearning:

    def run_classification_methods(self, filename):
        '''
        Perform machine learning on the csv file. Use the first 80% of the samples to train the model and the last 20% to test the model.
        Use the following algorithms: Logistic Regression, Random Forest, Support Vector Machine
        '''
        print("Running classification methods from the csv ", filename)
        # Read the csv file
        df = pd.read_csv(filename, header=None)
        # Split the data into features and labels
        gate_index = int(df.iat[0, 0])
        if gate_index == 0: # If the gate index is 0, then the gate is not included in the csv file and we need to use all the features
            X = df.iloc[:, 1:-1].values
            y = df.iloc[:, -1].values
        else:
            X = df.iloc[:, 1:gate_index].values 
            y = df.iloc[:, -1].values
            
        # Split the data into training and test sets (80% training, 20% test)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Scale the data
        scaler = StandardScaler()

        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        # Train the model
        models = []
        models.append(("LR", LogisticRegression()))
        models.append(("RF", RandomForestClassifier()))
        models.append(("DT", DecisionTreeClassifier()))

        for name, model in models:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            # Calculate confusion matrix
            cm = confusion_matrix(y_test, y_pred)
            print(name, " Confusion Matrix:")
            
            # Plot confusion matrix with labels "Acceptable", "Success", "Failure"
            sns.heatmap(cm, annot=True, fmt='g', xticklabels=["Acceptable", "Failure", "Sucess"], yticklabels=["Acceptable", "Failure", "Success"], cmap="Blues")
            plt.xlabel("Predicted")
            plt.ylabel("Actual")
            plt.title(name + " Confusion Matrix")
            # save plt to file
            plt.savefig("images/confusion_matrixes/" + filename + "_" + name + "_confusion_matrix.png")
            plt.show()
            print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))

    def run_regression_methods(self, filename):
        '''
        Perform machine learning on the csv file. Use the first 80% of the samples to train the model and the last 20% to test the model.
        Use the following algorithms: Linear Regression, Random Forest, Support Vector Machine, Decision Tree
        '''
        print("Running classification methods from the csv ", filename)
        # Read the csv file
        df = pd.read_csv(filename, header=None)
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
        models.append(("DT", DecisionTreeRegressor()))

        for name, model in models:
            model.fit(X_train, y_train)
            # Evaluate the model
            y_pred = model.predict(X_test)
            print(name, "R^2:", metrics.r2_score(y_test, y_pred))
            print(name, "MAE:", metrics.mean_absolute_error(y_test, y_pred))
            print(name, "MSE:", metrics.mean_squared_error(y_test, y_pred))
            print("Accuracy:", model.score(X_test, y_test))
            print()