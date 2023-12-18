import pandas as pd

# Step 2: Read the CSV file into a DataFrame
df = pd.read_csv('output_stage_2.csv')

# Step 3: Sort the DataFrame by the first string column
df_sorted = df.sort_values(by='Issue info')

# Optionally, Step 4: Save the sorted DataFrame back to a CSV file
df_sorted.to_csv('output_stage_3.csv', index=False)
