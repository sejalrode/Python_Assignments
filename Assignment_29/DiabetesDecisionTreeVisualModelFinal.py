import pandas as pd
import numpy as np

import seaborn as sns 
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousDecisionTree(datasetpath):
    line = "*" * 120
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
    print(line)
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
    #plt.show()

    #Heatmap to understand correlation
    plt.figure(figsize = (10,5))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Marvellous Correlation Heatmap")
    #plt.show()

    # Simple boxplots to identify outliers for each feature (excluding 'Outcome')
    for column in df.columns[:-1]:  # Exclude 'Outcome'
        plt.figure(figsize=(8, 6))
        plt.boxplot(df[column], patch_artist=True)
        plt.title(f"Boxplot of {column} (to detect outliers)")
        plt.ylabel(column)
        plt.grid(True)
        #plt.show()

    # Count zeros in each column
    print("Count of zeros per column:")
    print(line)
    print((df.drop(columns=['Outcome']) == 0).sum())
    print(line)

    print("Replacing zero values with mean :")
    print(line)
    # Store Outcome separately
    outcome = df['Outcome']
    # Replace 0s with NaN only in features (not in 'Outcome'), then fill NaNs with column mean
    df = df.drop(columns=['Outcome']).replace(0, np.nan)
    df = df.fillna(df.mean())
    # Reattach the Outcome column
    df['Outcome'] = outcome
    print(df)
    print(line)

    x = df.drop(columns = ['Outcome','BloodPressure','SkinThickness'])
    y = df['Outcome']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y ,test_size = 0.2, random_state = 42)

    model = DecisionTreeClassifier()
    
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
    #plt.show() 

    # Predict whether a patient is diabetic based on test data.
    test_df = pd.DataFrame(x_test, columns=x.columns)
    test_df['Actual_Outcome'] = y_test.values 
    test_df['Predicted_Outcome'] = y_pred

    #Display predictions on screen and save them in a CSV file.
    print(test_df)
    print(line)
    print("Predictions saved to 'Diabetes_Predictions_DecisionTree.csv'")
    test_df.to_csv("Diabetes_Predictions_DecisionTree.csv", index=False)

def main():
    MarvellousDecisionTree("diabetes.csv")

if __name__ == "__main__":
    main()