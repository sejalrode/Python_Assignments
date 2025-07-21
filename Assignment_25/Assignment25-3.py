# Apply label encoding to 'City' column.

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():
    data = {'City' : ['Pune','Mumbai','Delhi', 'Pune', 'Delhi']}
    
    df = pd.DataFrame(data)

    df['City'] = df['City'].map({'Pune' : 0, 'Mumbai' : 1, 'Delhi' : 2})

    print("Encoded data is : ")
    print(df)

if __name__ == "__main__":
    main()

'''
Encoded data is :
   City
0     0
1     1
2     2
3     0
4     2
'''

