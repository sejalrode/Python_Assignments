# Create a dataframe with 'Age' and 'Purchased' columns & split into train/test sets.

import pandas as pd
from sklearn.model_selection import train_test_split

def main():
  data = {'Age' : [22,25,47,52,46,56], 'Purchased' : [0,1,1,0,1,0]}

  df = pd.DataFrame(data)
  
  x = df['Age']
  y = df['Purchased']

  x_train,x_test,y_train,y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

  print("Training dataset : ")
  print(x_train)
  print(y_train)

  print("Testing dataset : ")
  print(x_test)
  print(y_test)

if __name__ == "__main__":
    main()

'''
Training dataset :
5    56
2    47
4    46
3    52
Name: Age, dtype: int64
5    0
2    1
4    1
3    0
Name: Purchased, dtype: int64

Testing dataset :
0    22
1    25
Name: Age, dtype: int64
0    0
1    1
Name: Purchased, dtype: int64
'''