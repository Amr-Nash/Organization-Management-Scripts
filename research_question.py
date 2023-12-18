import pandas as pd
import pyperclip

# Read the CSV file into a pandas DataFrame
csv_file = 'output_stage_1.csv'  # Replace with the actual CSV file path
out_csv_file = 'output_stage_2.csv'  # Replace with the actual CSV file path
df = pd.read_csv(csv_file)

# Iterate through each row
for index, row in df.iterrows():
    # Copy "Article Abstract" data to clipboard
    abstract_data = row['Article Abstract']
    question = f'''The following paragraph is the abstract paragraph of an article named {row['Article Name']}.
 The paragraph:\n{abstract_data}
 Give me the research methodology, in only  
'''
    pyperclip.copy(question)

    # Prompt user to input "Research Question"
    research_question = input(f"Enter Research Question for '{row['Article Name']}': ")

    # Update the DataFrame with the entered "Research Question"
    df.at[index, 'Research Question'] = research_question

# Save the updated DataFrame back to the CSV file
df.to_csv(out_csv_file, index=False)

print("Data has been updated.")
