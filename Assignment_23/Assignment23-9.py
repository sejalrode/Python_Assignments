#Create a df with missing values & fill them with column mean.

import pandas as pd
import numpy as np

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [np.nan,90,78],
        'Science':[92,np.nan,80]
        }

    df = pd.DataFrame(data)  # Convert dictionary to DataFrame

    print("Original DataFrame:")
    print(df)

    # Calculate mean only for numeric columns to avoid error
    column_means = df.mean(numeric_only=True)

    # Fill missing values with the respective column means
    df_filled = df.fillna(column_means)

    print("\nDataFrame after filling missing values with column means:")
    print(df_filled)

    #df.fillna(df.mean(numeric_only = True), inplace = True)

if __name__ == "__main__":
    main()

'''
Original DataFrame:
    Name  Math  Science
0   Amit   NaN     92.0
1  Sagar  90.0      NaN
2  Pooja  78.0     80.0

DataFrame after filling missing values with column means:
    Name  Math  Science
0   Amit  84.0     92.0
1  Sagar  90.0     86.0
2  Pooja  78.0     80.0
'''