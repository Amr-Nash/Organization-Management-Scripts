import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('output_stage_3_no_abstract.csv')

# Create an empty list to store the unique university names
authors = []

# Iterate through the columns and rows of the DataFrame
for column in df.columns:
    if column.startswith('Author'):
        # Extract unique values from the column and add them to the list
        authors.extend(df[column].dropna().unique())

# Remove any duplicate university names
authors = list(set(authors))


# Create a DataFrame with the 'Authors' column
df = pd.DataFrame({'Authors': authors})

# Save the DataFrame to a CSV file
df.to_csv('authors_list.csv', index=False)

print(f'The list of authors has been saved to authors_list.csv.')

# Print the list of authors
# print(authors)
