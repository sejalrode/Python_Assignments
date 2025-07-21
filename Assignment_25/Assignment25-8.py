# Fill missing values in a numeric column usimg interpolation.

import pandas as pd
import numpy as np

def main():
    data = {'Marks' : [85,np.nan,90,np.nan,95]}

    df = pd.DataFrame(data) 

    print("Original dataframe : ")
    print(df)

    df.interpolate(method='linear', axis = 0,inplace = True)
    print("\nData after interpolation : ")
    print(df)

if __name__ == "__main__":
    main()

'''
Original dataframe :
   Marks
0   85.0
1    NaN
2   90.0
3    NaN
4   95.0

Data after interpolation :
   Marks
0   85.0
1   87.5
2   90.0
3   92.5
4   95.0
'''