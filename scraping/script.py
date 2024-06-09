import os
import pandas as pd # type: ignore

csv_folder = '.'

output_csv = 'merged_output2.csv'

dfs = []

for file in os.listdir(csv_folder):
    if file.endswith('.csv'):
        file_path = file
        name_file=file_path.rstrip('.csv')
        nameArr = name_file.split("_")
        df = pd.read_csv(file_path)
        df['id'] = nameArr[0]
        df['Place Name'] = ' '.join(nameArr[1:])
        cols = ['id', 'Place Name'] + [col for col in df.columns if col not in ['id', 'Place Name']]
        df = df[cols]
        dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

merged_df.to_csv(output_csv, index=False)

print(f"All CSV files merged into {output_csv}")
