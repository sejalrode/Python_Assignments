# Detect the outliers in the 'Salary' Column using IQR method.

import pandas as pd
from scipy.stats import iqr

def main():
    data = {'Salary' : [25000,27000,29000,31000,50000,100000]}
    
    df = pd.DataFrame(data)

    # Calculate Q1 and Q3
    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)

    # Calculate IQR
    IQR_value = Q3 - Q1 

    # Calculate lower and upper bounds
    lower_bound = Q1 - 1.5 * IQR_value
    upper_bound = Q3 + 1.5 * IQR_value

    # Identify and filter out outliers
    df_cleaned = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]
    outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]

    print("Original DataFrame:")
    print(df)
    print("\nCleaned DataFrame (outliers removed):")
    print(df_cleaned)
    print("\nIdentified Outliers:")
    print(outliers)

if __name__ == "__main__":
    main()

'''
Original DataFrame:
   Salary
0   25000
1   27000
2   29000
3   31000
4   50000
5  100000

Cleaned DataFrame (outliers removed):
   Salary
0   25000
1   27000
2   29000
3   31000
4   50000

Identified Outliers:
   Salary
5  100000

'''