import pandas as pd
import numpy as np

import seaborn as sns 
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

def MarvellousDecisionTree():
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

    model = DecisionTreeClassifier()
    
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)

    plt.figure(figsize=(12,8))
    plot_tree(model,filled=True, feature_names=dataset.feature_names, class_names=dataset.target_names)
    plt.title("Marvellous Decision Tree classifier")
    plt.show()

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

    # Feature Importance as Horizontal Bar Chart
    importance = pd.Series(model.feature_importances_, index=x.columns)
    importance = importance.sort_values(ascending=True)   # sort ascending for better horizontal chart
    
    importance.plot(kind='barh', figsize=(10, 15), title='Feature Importance')
    plt.xlabel("Importance Score")
    plt.ylabel("Features")
    plt.tight_layout()
    plt.show()

    # Create a list of features with 0 importance
    zero_importance_features = importance[importance == 0.0].index.tolist()

    print(line)
    print("Features with 0 importance are (List):")
    print(zero_importance_features)
    print(line)

    print(line)
    print("Retraining model : ")
    x_selected = df.drop(columns = zero_importance_features + ['target'])
    x_selected_scaled = scaler.fit_transform(x_selected)

    X_train, X_test, Y_train, Y_test = train_test_split(x_selected_scaled, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy after dropping less important features: ", accuracy * 100)

def main():
    MarvellousDecisionTree()

if __name__ == "__main__":
    main()