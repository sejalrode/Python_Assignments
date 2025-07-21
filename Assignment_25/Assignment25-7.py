# Normailze the 'Age' column using Min-Max scaling.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():
    data = {'Age' : [18,22,25,30,35]}

    df = pd.DataFrame(data) 

    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()

    # Reshape required for single column (Math) as 2D array
    df['Age_Normalized'] = scaler.fit_transform(df[['Age']])

    print("Original + Normalized Age:\n")
    print(df)

if __name__ == "__main__":
    main()

'''
Original + Normalized Age:

   Age  Age_Normalized
0   18        0.000000
1   22        0.235294
2   25        0.411765
3   30        0.705882
4   35        1.000000

'''