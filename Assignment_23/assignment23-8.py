# Plot a line chart of marks for 'Amit' across all subjects.

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

     # Filter the row where Name is 'Amit', then select only the subject columns
    amit_marks = df[df['Name'] == 'Amit'][['Math', 'Science', 'English']].values.flatten()
    #print(amit_marks)

    subjects = ['Math','Science','English']
    
    plt.plot(subjects, amit_marks, marker = 'o')
    plt.xlabel('Subjects')
    plt.ylabel('Amit Marks')
    plt.title('Line Chart of Amit Report')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

'''

'''