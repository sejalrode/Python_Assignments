# Add a new column 'Total' to the dataframe as the sum of all subject marks.

import pandas as pd

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data)  # Convert dictionary to DataFrame

    df['Total'] = df['Math'] + df['Science'] + df['English']

    print(df)

if __name__ == "__main__":
    main()

'''
    Name  Math  Science  English  Total
0   Amit    85       92       75    252
1  Sagar    90       88       85    263
2  Pooja    78       80       82    240
'''