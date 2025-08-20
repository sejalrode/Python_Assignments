import pandas as pd
import numpy as np

import seaborn as sns 
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousLogistic():
    line = "*" * 120
    dataset = load_breast_cancer()

    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    df['target'] = dataset.target

    print(line)
    print("Dimention of dataframe",df.shape)
    print(line)

    print("Initial data is : ")
    print(line)
    print(df.head())
    print(line)

    print("Columns info : ")
    print(line)
    print(df.info())
    print(line)

    print("Null values in the dataset : ")
    print(line)
    print(df.isnull().sum())
    print(line)

    #Heatmap to understand correlation
    plt.figure(figsize = (50,25))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Marvellous Correlation Heatmap")
    plt.show()

    x = df.drop(columns = ['target'])
    y = df['target']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y ,test_size = 0.2, random_state = 42)

    model = LogisticRegression()
    
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy is : ",accuracy*100)
    print(line)

    Conf_matrix = confusion_matrix(y_test,y_pred)
    print("Confusion matrix is : ")
    print(line)
    print(Conf_matrix)
    print(line)

    report = classification_report(y_test,y_pred)
    print("Classification report is : ")
    print(line)
    print(report)
    print(line)

    # Visualizing the confusion matrix
    plt.figure(figsize=(6, 5))
    sns.heatmap(Conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Predicted 0', 'Predicted 1'], yticklabels=['Actual 0', 'Actual 1'])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show() 

def main():
    MarvellousLogistic()

if __name__ == "__main__":
    main()