import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    line = "*" * 120
    df = pd.read_csv("breast-cancer-wisconsin.csv")

    print(line)
    print("Dataset loaded successfully")
    print(line)
    print(df.head())

    print(line)
    print("Dimensions of dataset : ",df.shape)
    print(line)

    print("Cleaning the dataset : ")
    print(line)
    df.drop(columns = ["CodeNumber"], inplace = True)
    print("Updated dataset is : ")
    print(line)
    print(df.head())
    print(line)

    print("Replacing null values : ")
    df.replace('?', np.nan, inplace=True)
    print("Missing values in each column : \n",df.isnull().sum())
    print(line)
    df['BareNuclei'] = pd.to_numeric(df['BareNuclei'], errors='coerce')
    df['BareNuclei'].fillna(df['BareNuclei'].mean(), inplace=True)
    print(line)


    x = df.drop(columns = ["CancerType"])
    y = df["CancerType"]

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)
    
    X_train,X_test,Y_train,Y_test = train_test_split(x_scale, y, test_size = 0.2, random_state = 42)

    model = DecisionTreeClassifier()

    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy is : ",accuracy*100)
    cm = confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix : \n",cm)

    # Visualizing the confusion matrix
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Predicted 0', 'Predicted 1'], yticklabels=['Actual 0', 'Actual 1'])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show() 

    plt.figure(figsize=(12,8))
    plot_tree(model,filled=True, feature_names=x.columns, class_names=["Benign", "Malignant"])
    plt.title("Marvellous Decision Tree classifier")
    plt.show()

    importance = pd.Series(model.feature_importances_,index = x.columns)
    importance = importance.sort_values(ascending=False)
    importance.plot(kind = 'bar', figsize = (10,6), title = 'Feature Importance')
    plt.show()

    print(line)
    print("Retraining model : ")
    x_selected = df.drop(columns = ["Mitoses","NormalNucleoli","MarginalAdhesion"])
    x_selected_scaled = scaler.fit_transform(x_selected)

    X_train, X_test, Y_train, Y_test = train_test_split(x_selected_scaled, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy after dropping less important features: ", accuracy * 100)

if __name__ == "__main__":
    main()