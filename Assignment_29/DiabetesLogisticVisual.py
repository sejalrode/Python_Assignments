import pandas as pd
import numpy as np

import seaborn as sns 
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

def MarvellousLogistic(datasetpath):
    line = "*" * 90
    df = pd.read_csv(datasetpath)

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

    print("Basic statistical information : ")
    print(df.describe())
    print(line)

    # Histogram of Outcome using matplotlib
    plt.figure(figsize=(6, 4))
    plt.hist(df['Outcome'], bins=2, color='skyblue', edgecolor='black', rwidth=0.8)
    plt.title('Distribution of Outcome Variable')
    plt.xlabel('Outcome (0 = No Diabetes, 1 = Diabetes)')
    plt.ylabel('Count')
    plt.xticks([0, 1])
    plt.grid(axis='y')
    plt.show()

    # Simple boxplots to identify outliers for each feature (excluding 'Outcome')
    for column in df.columns[:-1]:  # Exclude 'Outcome'
        plt.figure(figsize=(8, 6))
        plt.boxplot(df[column], patch_artist=True)
        plt.title(f"Boxplot of {column} (to detect outliers)")
        plt.ylabel(column)
        plt.grid(True)
        plt.show()

    #Heatmap to understand correlation
    plt.figure(figsize = (10,5))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Marvellous Correlation Heatmap")
    plt.show()


def main():
    MarvellousLogistic("diabetes.csv")

if __name__ == "__main__":
    main()