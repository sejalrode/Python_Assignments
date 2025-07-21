# Normailze the 'Math' scores using Min-Max scaling.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data) 

    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()

    # Reshape required for single column (Math) as 2D array
    df['Math_Normalized'] = scaler.fit_transform(df[['Math']])

    print("Original + Normalized Math Scores:\n")
    print(df)

if __name__ == "__main__":
    main()

'''
Original + Normalized Math Scores:

    Name  Math  Science  English  Math_Normalized
0   Amit    85       92       75         0.583333
1  Sagar    90       88       85         1.000000
2  Pooja    78       80       82         0.000000
'''