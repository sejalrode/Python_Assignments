# Group students by 'Gender' & calculate avg marks.

import pandas as pd

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(data) 
    df['Gender'] = ['Male', 'Male', 'Female']

    print("Original DataFrame:")
    print(df)

    # Group by 'Gender' and calculate average marks
    grouped_data = df.groupby('Gender').mean(numeric_only=True)
    print("\nAverage Marks by Gender:")
    print(grouped_data)

if __name__ == "__main__":
    main()

'''
Original DataFrame:
    Name  Math  Science  English  Gender
0   Amit    85       92       75    Male
1  Sagar    90       88       85    Male
2  Pooja    78       80       82  Female

Average Marks by Gender:
        
        Math  Science  English
Gender
Female  78.0     80.0     82.0
Male    87.5     90.0     80.0
'''
