import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('output_stage_3.csv')

# Specify the column you want to delete
column_to_delete = 'Article Abstract'

# Delete the specified column
df = df.drop(column_to_delete, axis=1)

# Specify the column you want to move and its desired position
# Theme_Analysis = 'Theme Analysis'
# Research_Methodology = 'Research Methodology'
# theme_position = 2  # 0-based index, so 1 corresponds to the second position
# research_position = 3  # 0-based index, so 1 corresponds to the second position
#
# # Get the list of columns
# columns = df.columns.tolist()
#
# # Remove the desired column from its current position
# columns.remove(desired_column)
#
# # Insert the desired column at the desired position
# columns.insert(desired_position, desired_column)
#
# # Create a new DataFrame with columns in the desired order
# df = df[columns]

# Save the modified DataFrame back to a new CSV file
df.to_csv('output_stage_3_no_abstract.csv', index=False)

