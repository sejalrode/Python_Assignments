# Create a bar plot of student names vs total marks.

import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data)  # Convert dictionary to DataFrame

    df['Total'] = df['Math'] + df['Science'] + df['English']

    plt.bar(df['Name'], df['Total'])
    plt.xlabel('Student names')
    plt.ylabel('Total marks')
    plt.title('Bar Plot')
    plt.show()
    

if __name__ == "__main__":
    main()
