import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score, confusion_matrix

def WinePredictor(Datapath):
    df = pd.read_csv(Datapath)

    df.dropna(inplace = True)

    x = df.drop(columns = ['Class'])
    y = df['Class']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)
    
    x_train,x_test,y_train,y_test = train_test_split(x_scale, y, test_size = 0.2, random_state = 42)

    #Parameter Tuning
    accuracy_scores = []
    k_range = range(1,21)

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors = k)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        Accuracy = accuracy_score(y_test, y_pred)
        accuracy_scores.append(Accuracy)

    plt.figure(figsize = (8,5))
    plt.plot(k_range, accuracy_scores, marker = 'o', linestyle = '--')
    plt.title("Accuracy VS K-Value")
    plt.xlabel("Value of k")
    plt.ylabel("Accuracy of model")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is : ",best_k)

    #Final Model Training
    model = KNeighborsClassifier(n_neighbors = best_k)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    Accuracy = accuracy_score(y_test, y_pred)
    print("Final best accuracy is : ",Accuracy*100)

    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix : \n",cm)
    
def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()
