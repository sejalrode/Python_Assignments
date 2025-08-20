import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def DatasetLoad(Datasetpath):
    line = "*" * 150
    df = pd.read_csv(Datasetpath,sep=';')  # semicolon is common in European CSVs)

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
    print("Null values : ",df.isnull().sum().sum())
    print(line)

    print("Basic statistical information : ")
    print(df.describe())
    print(line)

    print("Replacing unknown values with mode : ")
    print(line)
    # Replace 'unknown' with mode in specific columns
    for col in ['job', 'education', 'poutcome']:
        df[col] = df[col].replace('unknown', df[col].mode()[0])
    print(df.head())
    print(line)

    return df

def DatasetPreprocess(df):
    line = "*" * 150
    print("Remove unknown columns : ")
    print(line)
    df.drop(columns = ['contact','poutcome'],inplace = True)
    print(df.head())
    print(line)

    print("Encoding the dataset : ")
    print(line)
    LE = LabelEncoder()
    categorical_cols = ['job', 'marital', 'education', 'default','housing','loan','month','y']
    for col in categorical_cols:
        df[col] = LE.fit_transform(df[col])
    print(df.head())
    print(line)

    return df

def DatasetSplit(df):
    x = df.drop(columns = ['y'])
    y = df['y']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y ,test_size = 0.2, random_state = 42)

    return x_train, x_test, y_train, y_test

def BankLogistic(x_train, x_test, y_train, y_test):
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

    return y_pred,y_test

def ModelEvaluation(y_pred,y_test):
    line = "*" * 150

    Accuracy = accuracy_score(y_test, y_pred)
    print("Final best accuracy is : ",Accuracy*100)
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

def main():
    df = DatasetLoad("bank-full.csv")

    df = DatasetPreprocess(df)

    x_train, x_test, y_train, y_test = DatasetSplit(df)

    y_pred,y_test = BankLogistic(x_train, x_test, y_train, y_test)

    ModelEvaluation(y_pred,y_test)

if __name__ == "__main__":
    main()