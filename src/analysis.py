import pandas as pd

data = pd.read_csv('../dataset/processed_data/cleaned_data.csv')

top_countries = data.groupby('Country')['Visitors'].sum().sort_values(ascending=False)

print(top_countries.head())