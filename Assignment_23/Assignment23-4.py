# Display students who scored more than 85 in Science.

import pandas as pd

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data)  # Convert dictionary to DataFrame

    print("Students who scored more than 85 in Science : ")

    print(df[df['Science'] > 85])

if __name__ == "__main__":
    main()

'''
Students who scored more than 85 in Science :

    Name  Math  Science  English
0   Amit    85       92       75
1  Sagar    90       88       85 
'''