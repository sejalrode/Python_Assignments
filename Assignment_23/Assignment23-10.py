#Drop 'English' column from original dataframe.

import pandas as pd

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data)  # Convert dictionary to DataFrame

    print(df)

    df_new = df.drop(columns = ['English'])

    print(df_new)

if __name__ == "__main__":
    main()

'''

'''