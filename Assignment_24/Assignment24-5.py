# Add a new column 'Status' where students with total >= 250 are 'Pass' else 'Fail'.

import pandas as pd

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data) 

    df['Total'] = df['Math'] + df['Science'] + df['English']
    
    # Condition: total >= 250 means Pass, else Fail
    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')

    print(df)
    
if __name__ == "__main__":
    main()

'''
    Name  Math  Science  English  Total Status
0   Amit    85       92       75    252   Pass
1  Sagar    90       88       85    263   Pass
2  Pooja    78       80       82    240   Fail

'''