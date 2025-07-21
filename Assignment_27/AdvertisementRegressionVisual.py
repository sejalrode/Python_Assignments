#Multiple Independent variable : Multiple Linear Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

def MarvellousAdvertise(Datapath):
    Line = "*" * 80

    df = pd.read_csv(Datapath)

    print(Line)
    print("First few records of the dataset are : ")
    print(Line)
    print(df.head())
    print(Line)

    print("Clean the dataset : ")
    df.drop(columns = ['Unnamed: 0'], inplace = True)
    print("Updated dataset is : ")
    print(Line)
    print(df.head())
    print(Line)

    print("Missing values in each column : \n",df.isnull().sum())
    print(Line)

    print("Statistical Summary : ")
    print(Line)
    print(df.describe())
    print(Line)

    print("Correlation Matrix : ")
    print(Line)
    print(df.corr()) #Correlation b/w Tv & sales is highest( 0.782224)
    print(Line)

    plt.figure(figsize = (10,5))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Marvellous Correlation Heatmap")
    plt.show()

    sns.pairplot(df)
    plt.suptitle("Pairplot of Features : ", y = 1.02)
    plt.show()

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()