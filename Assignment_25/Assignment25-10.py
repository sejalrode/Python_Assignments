# Split the dataframe into multiple features into train-test for supervised learning .

import pandas as pd
from sklearn.model_selection import train_test_split

def main():
  data = {'Age' : [25,30,45,35,22],
          'Salary' : [50000, 60000, 80000, 65000, 45000] ,
          'Purchased' : [1,0,1,0,1]}

  df = pd.DataFrame(data)
  
  x = df[['Age','Salary']]
  y = df['Purchased']

  x_train,x_test,y_train,y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

  print("Training dataset : ")
  print("x_train : ",x_train)
  print("y_train : ",y_train)

  print("Testing dataset : ")
  print("x_test : ",x_test)
  print("y_test :",y_test)

if __name__ == "__main__":
    main()

'''
Training dataset :
x_train :     Age  Salary
4   22   45000
2   45   80000
0   25   50000
3   35   65000

y_train :  4    1
2    1
0    1
3    0
Name: Purchased, dtype: int64


Testing dataset :
x_test :     Age  Salary
1   30   60000

y_test : 1    0
Name: Purchased, dtype: int64
'''