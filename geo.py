import pandas as pd
from geopy.geocoders import Nominatim


# Function to get the country of a university
def get_country(university):
    geolocator = Nominatim(user_agent="university_locator")
    try:
        location = geolocator.geocode(university)
        if location:
            return location.address.split(",")[-1].strip()
    except Exception as e:
        print(f"Error while geocoding {university}: {e}")
    return None


# Load the existing CSV file or create a new one
try:
    df = pd.read_csv('universities_list.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=['Universities', 'Country'])

# Find the index of the first row with an empty 'Country' column
start_index = df[df['Country'].isnull()].index.min()

# If start_index is NaN, it means all universities have a country, start from the beginning
if pd.isna(start_index):
    start_index = 0

# Iterate through the universities starting from the first one with an empty country
for index, row in df.loc[start_index:].iterrows():
    university = row['Universities']
    country = row['Country']

    # If the country is empty, fetch it
    if pd.isna(country):
        country = get_country(university)
        df.at[index, 'Country'] = country

        # Save the progress and exit if an error occurs
        df.to_csv('universities_list.csv', index=False)
        print(f"Progress saved. Resuming from index {index + 1}.")
        # exit()

# Save the final DataFrame to a CSV file
df.to_csv('universities_list.csv', index=False)
print('The list of universities with countries has been saved to universities_list.csv.')
