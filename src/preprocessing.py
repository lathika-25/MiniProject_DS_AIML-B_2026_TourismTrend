import pandas as pd

data = pd.read_csv('../dataset/raw_data/Country Wise Yearly VIsitors.csv')

data_long = data.melt(id_vars=['Country'], 
                      var_name='Year', 
                      value_name='Visitors')

data_long['Year'] = data_long['Year'].astype(int)

data_long.to_csv('../dataset/processed_data/cleaned_data.csv', index=False)