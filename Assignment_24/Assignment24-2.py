# Create a 'Gender' column & perform one-hot encoding.

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science':[92,88,80],
        'English' : [75,85,82]
        }

    df = pd.DataFrame(data) 

    df['Gender'] = ['Male','Male','Female']

    print(df)

    # Initialize OneHotEncoder
    encoder = OneHotEncoder(handle_unknown = 'ignore')
    
    # Fit and transform the categorical column
    encoded_data = encoder.fit_transform(df[['Gender']])

    # Create a DataFrame from the encoded data
    encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(['Gender']))

    print(encoded_df)

    
if __name__ == "__main__":
    main()

'''
 Name  Math  Science  English  Gender
0   Amit    85       92       75    Male
1  Sagar    90       88       85    Male
2  Pooja    78       80       82  Female
   
   Gender_Female  Gender_Male
0            0.0          1.0
1            0.0          1.0
2            1.0          0.0

'''