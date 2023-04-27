import numpy as np
import pandas as pd
from sklearn import linear_model, metrics, svm, tree
from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso


def machine_learning():
    '''
    Perform machine learning on the csv file. Use the first 80% of the samples to train the model and the last 20% to test the model.
    Use the following algorithms: Logistic Regression, Random Forest, Support Vector Machine
    '''
    # Read the csv file
    df = pd.read_csv("samples.csv", header=None)
    # Split the data into features and labels
    X = df.iloc[:, :-30].values 
    y = df.iloc[:, -1].values
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # Scale the data. This is necessary for SVM, because it uses the euclidean distance.
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    # Train the model
    models = []
    models.append(("LR", linear_model.LogisticRegression()))
    models.append(("RF", RandomForestClassifier()))
    models.append(("SVM", svm.SVC()))
    for name, model in models:
        model.fit(X_train, y_train)
        # Evaluate the model
        y_pred = model.predict(X_test)
        print(name, ":", metrics.classification_report(y_test, y_pred))


def machine_learning2():
    '''
    Perform machine learning on the csv file. Use the first 80% of the samples to train the model and the last 20% to test the model.
    Use the following algorithms: Logistic Regression, Random Forest, Support Vector Machine
    '''
    # Read the csv file
    df = pd.read_csv("samples.csv", header=None)
    # Split the data into features and labels
    X = df.iloc[:, :-30].values 
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
    models.append(("Ridge", Ridge()))
    models.append(("Lasso", Lasso()))
    for name, model in models:
        model.fit(X_train, y_train)
        # Evaluate the model
        y_pred = model.predict(X_test)
        
        # Calculate the metrics
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        # Print the performance metrics
        print(f"{name} :")
        print(f"  Mean Absolute Error (MAE): {mae:.4f}")
        print(f"  Mean Squared Error (MSE): {mse:.4f}")
        print(f"  Root Mean Squared Error (RMSE): {rmse:.4f}")
        print()
