import os
import pandas as pd # type: ignore

csv_folder = '.'

output_csv = 'Comments_twitter.csv'

dfs = []

for file in os.listdir(csv_folder):
    if file.endswith('.csv'):
        file_path = os.path.join(csv_folder, file)
        df = pd.read_csv(file_path)
        dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)
merged_df = merged_df.sort_values(by='id')
merged_df = merged_df.drop_duplicates(subset=['full_text'])
merged_df.to_csv(output_csv, index=False)