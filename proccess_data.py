import pandas as pd
import os

data_folder = './data'
output_file = 'single-formatted_data.csv'
all_data = []

for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder, filename)
        df = pd.read_csv(file_path)
        all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)

clean_df = combined_df[combined_df['product'].str.lower() == 'pink morsel'].copy()
clean_df['price'] = clean_df['price'].str.replace('$', '', regex=False).astype(float)
clean_df['sales'] = clean_df['price'] * clean_df['quantity']
clean_df = clean_df[['sales', 'date', 'region']]

clean_df.to_csv(output_file, index=False)

print(f"Done! The data already saved into {output_file}")