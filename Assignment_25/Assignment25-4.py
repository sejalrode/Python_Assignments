# Apply one-hot encoding to 'Department' column.

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():
    data = {'Department' : ['HR', 'IT', 'Finance' ,'HR','IT']}

    df = pd.DataFrame(data) 
    print(df)

    # Initialize OneHotEncoder
    encoder = OneHotEncoder(handle_unknown = 'ignore')
    
    # Fit and transform the categorical column
    encoded_data = encoder.fit_transform(df[['Department']])

    # Create a DataFrame from the encoded data
    encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(['Department']))

    print("\nDataset after OneHot Encoding : ")
    print(encoded_df)
   
if __name__ == "__main__":
    main()

'''
 Department
0         HR
1         IT
2    Finance
3         HR
4         IT

Dataset after OneHot Encoding :
   Department_Finance  Department_HR  Department_IT
0                 0.0            1.0            0.0
1                 0.0            0.0            1.0
2                 1.0            0.0            0.0
3                 0.0            1.0            0.0
4                 0.0            0.0            1.0
'''