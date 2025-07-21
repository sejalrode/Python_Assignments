#Replace multiple values in a column using a dictionary.

import pandas as pd

def main():
  data = {'Grade' : ['A+','B','A','C','B+']}

  df = pd.DataFrame(data)
  print(df)
  
  df['Grade'] = df['Grade'].replace({
        'A+': 'Excellent',
        'A' : 'Very Good',
        'B+': 'Good',
        'B' : 'Average',
        'C' : 'Poor'
    })
  print("Updated dataset is : ")
  print(df)

if __name__ == "__main__":
    main()

'''
  Grade
0    A+
1     B
2     A
3     C
4    B+

Updated dataset is :
       Grade
0  Excellent
1    Average
2  Very Good
3       Poor
4       Good
'''