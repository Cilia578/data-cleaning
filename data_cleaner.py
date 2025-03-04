import pandas as pd
import numpy as np


file_path = "customer_transactions.csv" 
df = pd.read_csv(file_path) 

print("Raw Data:")
print(df.head())


numeric_cols = df.select_dtypes(include=[np.number]).columns 
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())


for col in df.select_dtypes(include=['object']).columns: 
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nData after handling missing values:")
print(df.head())

df.drop_duplicates(inplace=True)

print("\nData after removing duplicates:")
print(df.head())

df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].min()) / (df[numeric_cols].max() - df[numeric_cols].min())

print("\nData after normalization:")
print(df.head())

output_file = "cleaned_data.csv"
df.to_csv(output_file, index=False) 

print(f"\nCleaned data saved to {output_file}")