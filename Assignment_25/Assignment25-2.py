# Detect column datatypes and convert 'Age' from float to int.

import pandas as pd

def main():
    data = {'Name' : ['A','B','C'],'Age' : [21.0,22.0,23.0]}
    
    df = pd.DataFrame(data)

    print(df.dtypes) 

    df['Age'] = df['Age'].astype(int)

    print("\nConverting 'Age' from float to int.")
    print(df)

if __name__ == "__main__":
    main()

'''
Name     object
Age     float64
dtype: object

Converting 'Age' from float to int.
  Name  Age
0    A   21
1    B   22
2    C   23
'''