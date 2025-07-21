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


    x = df[['TV','radio','newspaper']]
    y = df['sales']

    x_train,x_test,y_train,y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    model = LinearRegression()
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    MSE = metrics.mean_squared_error(y_test, y_pred)
    RMSE = np.sqrt(MSE)
    R2 = metrics.r2_score(y_test, y_pred)

    print("Mean Squared Error is : ",MSE)
    print("Root Mean Squared Error is : ",RMSE)
    print("R Square Value : ",R2)

    print(Line)
    print("Model Coefficient are : ")
    print(Line)
    for col, coef in zip(x.columns, model.coef_):
        print(f"{col} : {coef}")

    print(Line)
    print("Y Intercept is : ",model.intercept_)

    plt.figure(figsize = (8,5))
    plt.scatter(y_test , y_pred, color = 'blue')
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Marvellous Advertisement")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()