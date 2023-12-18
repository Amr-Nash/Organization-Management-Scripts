import pandas as pd
import pyperclip

csv_file = 'articles_list.csv'

try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"The file '{csv_file}' does not exist. Creating a new DataFrame.")
    df = pd.DataFrame(columns=['Articles', 'Theme Analysis', 'Level of Analysis', 'Research Methodology'])

# Find the index of the first row with an empty 'Gender' column
start_index = df[df['Theme Analysis'].isnull()].index.min()

# If start_index is NaN, it means all rows have a gender, start from the beginning
if pd.isna(start_index):
    start_index = 0

for index, row in df.loc[start_index:].iterrows():
    article = row['Articles']
    pyperclip.copy(f'''The following is a text from the article "{article}" I want you to provide me with the 'Theme Analysis' in less than 20 words, 'Level of Analysis' in either of those three values (Individual / Organizational / Industry Field), and the 'Research Methodology' in either of those two values(Qualitative / Quantitative) separate the resultes with this charector '|'
please give simple answers.  
with values only
without the keys
The Text:\n ''')

    values = input(f"Enter the values for '{article}' separated by '|' : ")

    values_list = values.split('|')

    # Update 'Gender' column based on user input
    df.at[index, 'Theme Analysis'] = values_list[0].strip()
    df.at[index, 'Level of Analysis'] = values_list[1].strip()
    df.at[index, 'Research Methodology'] = values_list[2].strip()

    # Save the progress and exit
    df.to_csv(csv_file, index=False)
    print(f"Progress saved. Resuming from index {index + 1}.")
exit()

print("All rows have been processed.")
