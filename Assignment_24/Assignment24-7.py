# Export the final Dataframe to a CSV file.

import pandas as pd

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data) 

    df['Total'] = df[['Math','Science','English']].sum(axis = 1)
    
    # Condition: total >= 250 means Pass, else Fail
    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')

    df.to_csv('Students.csv', index=False)
    print("CSV file 'Students.csv' has been created.")

if __name__ == "__main__":
    main()

