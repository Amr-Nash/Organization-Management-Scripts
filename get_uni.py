import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('output_stage_3_no_abstract.csv')

# Create an empty list to store the unique university names
universities = []

# Iterate through the columns and rows of the DataFrame
for column in df.columns:
    if column.startswith('Institute'):
        # Extract unique values from the column and add them to the list
        universities.extend(df[column].dropna().unique())

# Remove any duplicate university names
universities = list(set(universities))

# Print the list of universities
print(universities)
