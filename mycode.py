import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

new_row= [
    {'Name': 'David', 'Age': 28, 'City': 'San Francisco'}
]
df = pd.concat([df, pd.DataFrame(new_row)], ignore_index=True)

new_row2= [
    {'Name': 'Ravi', 'Age': 58, 'City': 'San Jose'}
]
df = pd.concat([df, pd.DataFrame(new_row2)], ignore_index=True)


data_dir = 'data'

os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file will be saved to: {file_path}")