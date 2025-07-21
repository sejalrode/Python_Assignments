# Plot a boxplot for English marks to check distribution & outliers.

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
    plt.boxplot(df['English'], patch_artist=True)
    plt.title("Distribution of English Marks")
    plt.ylabel("English Marks")
    plt.show()
    
if __name__ == "__main__":
    main()

