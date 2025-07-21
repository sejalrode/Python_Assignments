# Replace values in 'Marks' less than 50 with 'Fail' using where().

import pandas as pd
import numpy as np

def main():
    data = {'Marks' : [45,67,88,32,76]}

    df = pd.DataFrame(data) 

    print("Original dataset : ")
    print(df)

    df['Marks'] = df['Marks'].where(df['Marks'] >= 50, other='Fail')
    print("\nUpdated dataset : ")
    print(df)

if __name__ == "__main__":
    main()

'''
Original dataset :
   Marks
0     45
1     67
2     88
3     32
4     76

Updated dataset :
  Marks
0  Fail
1    67
2    88
3  Fail
4    76
'''