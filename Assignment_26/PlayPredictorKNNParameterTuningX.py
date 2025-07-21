import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score, confusion_matrix

def MarvellousKNN(Datapath):
    line = "*" * 50
    df = pd.read_csv(Datapath)

    print(line)
    print("Dataset loaded successfully : ")
    print(line)
    print(df.head())

    print(line)
    print("Dimensions of dataset : ",df.shape)
    print(line)

    print("Cleaning the dataset : ")
    print(line)
    df.drop(columns = ["Unnamed: 0"], inplace = True)
    print(df.head())
    print(line)

    print("Encoding the dataset : ")
    print(line)
    df['Whether'] = df['Whether'].map({'Sunny' : 0, 'Overcast' : 1, 'Rainy' : 2})
    df['Temperature'] = df['Temperature'].map({'Hot' : 0, 'Mild' : 1, 'Cool' : 2})
    df['Play'] = df['Play'].map({'No' : 0, 'Yes' : 1})
    print(df.head())
    print(line)
    
    x = df.drop(columns = ['Play'])
    y = df['Play']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size = 0.2, random_state = 42)

    #Parameter Tuning
    accuracy_scores = []
    k_range = range(1,21)

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors = k)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        Accuracy = accuracy_score(y_test, y_pred)
        accuracy_scores.append(Accuracy)

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is : ",best_k)

    #Final Model Training
    model = KNeighborsClassifier(n_neighbors = best_k)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    Accuracy = accuracy_score(y_test, y_pred)
    print("Final best accuracy is : ",Accuracy*100)

    cm = confusion_matrix(y_test, y_pred)
    print(line)
    print("Confusion Matrix : \n",cm)

def main():
    MarvellousKNN("PlayPredictor.csv")

if __name__ == "__main__":
    main()