import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import VotingClassifier


def main():
    line = "*" * 120

    print("Load the datasets : ")
    fake_df = pd.read_csv("Fake.csv")
    true_df = pd.read_csv("True.csv")

    print("Add label column : ")
    print(line)
    fake_df["label"] = 0
    print(fake_df.head())
    print(line)
    true_df["label"] = 1
    print(true_df.head())
    print(line)

    print("Combine the datastes : ")
    print(line)
    df = pd.concat([fake_df, true_df], axis=0)
    print(df.head())
    print(line)

    print("Reset index : ")
    print(line)
    df = df.reset_index(drop=True)
    print(df.head())
    print(line)

    print("Drop null values : ")
    df.dropna(inplace  = True)
    print(line)

    print("Keep only relevant columns (title, text, label) : ")
    print(line)
    df = df[["title", "text", "label"]]
    print(df.head())
    print(line)

    # Step 1: Choose what text to use (title, text, or both)
    # Here I’ll use only the "text" column
    print("TF-IDF : ")
    print(line)
    X_text = df["text"]
    Y = df["label"]

    # Step 2: Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

    # Step 3: Fit and transform the text data
    X = vectorizer.fit_transform(X_text)

    print("Shape of TF-IDF matrix:", X.shape)  # (rows, features)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)
    
    log_clf = LogisticRegression()
    dt_clf = DecisionTreeClassifier(max_depth=8)

    voting_clf = VotingClassifier(
        estimators=[
            ('lr', log_clf),
            ('dt', dt_clf)
        ],
        voting = 'hard'
    )

    voting_clf.fit(X_train,Y_train)
    
    y_pred = voting_clf.predict(X_test)

    print(line)
    print("Accuracy : ",accuracy_score(Y_test,y_pred) * 100)
    print(line)

    print(classification_report(Y_test, y_pred))
    print(line)

    print(line)
    cm = confusion_matrix(Y_test, y_pred)
    print("Confusion Matrix : \n",cm)

    # Visualizing the confusion matrix
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Predicted 0', 'Predicted 1'], yticklabels=['Actual 0', 'Actual 1'])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show() 

if __name__ == "__main__":
    main()