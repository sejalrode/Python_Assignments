#Create a Dataframe for student marks & print basic information like shape,columns & dtattypes.

import pandas as pd

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data)  # Convert dictionary to DataFrame

    print("Shape of DataFrame:", df.shape)
    print("Columns in DataFrame:", df.columns)
    print("Data types of each column:\n", df.dtypes)

if __name__ == "__main__":
    main()

'''
Shape of DataFrame: (3, 4)

Columns in DataFrame: Index(['Name', 'Math', 'Science', 'English'], dtype='object')

Data types of each column:
 Name       object
Math        int64
Science     int64
English     int64
dtype: object
'''