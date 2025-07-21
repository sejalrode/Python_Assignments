# Replace 'pooja' with 'puja' in 'Name' column .

import pandas as pd

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data)  # Convert dictionary to DataFrame

    df['Name'] = df['Name'].replace('Pooja', 'Puja')
    
    print(df)

if __name__ == "__main__":
    main()

'''
    Name  Math  Science  English
0   Amit    85       92       75
1  Sagar    90       88       85
2   Puja    78       80       82  
'''