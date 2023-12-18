import pandas as pd
import pyperclip

csv_file = 'authors_list.csv'

try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"The file '{csv_file}' does not exist. Creating a new DataFrame.")
    df = pd.DataFrame(columns=['Authors', 'Gender'])

# Find the index of the first row with an empty 'Gender' column
start_index = df[df['Gender'].isnull()].index.min()

# If start_index is NaN, it means all rows have a gender, start from the beginning
if pd.isna(start_index):
    start_index = 0

for index, row in df.loc[start_index:].iterrows():
    author = row['Authors']
    pyperclip.copy(author)

    gender = input(f"Enter the gender for '{author}' (1 for male, any other value for female): ")

    # Update 'Gender' column based on user input
    df.at[index, 'Gender'] = 'male' if gender == '1' else 'female'

    # Save the progress and exit
    df.to_csv(csv_file, index=False)
    print(f"Progress saved. Resuming from index {index + 1}.")
exit()

print("All rows have been processed.")
