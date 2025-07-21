# Plot a histogram of 'Maths' marks.

import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data) 

    plt.figure(figsize=(8, 6))
    plt.hist(df['Math'], bins=5, color='skyblue', edgecolor='black')
    plt.title("Distribution of Math Marks")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.show()
    
if __name__ == "__main__":
    main()

