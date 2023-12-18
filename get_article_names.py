import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('output_stage_3_no_abstract.csv', index_col="Index")

# Create an empty list to store the unique university names
# articles = []
#
# # Iterate through the columns and rows of the DataFrame
# for column in df.columns:
#     if column.startswith('Article Name'):
#         # Extract unique values from the column and add them to the list
#         articles.extend(df[column].dropna().unique())
#
# # Remove any duplicate university names
# articles = list(set(articles))


# Create a DataFrame with the 'Authors' column
df_subset = df[['Article Name']]

# Save the DataFrame to a CSV file
df_subset.to_csv('articles_list.csv', index=False)

print(f'The list of articles has been saved to articles_list.csv.')

# Print the list of articles
# print(articles)
