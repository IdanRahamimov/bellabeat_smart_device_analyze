# This script was made to merge the csv files with data by the minute because its 
# the file is too big to load manually 

import os
import pandas as pd

# Specify the directory
DIRECTORY = "../data_april12_to_may12_2016"

def merge(directory):
    # Get a list of all files in the directory with 'minute' in their name
    csv_files = [f for f in os.listdir(directory) if 'minute' in f]

    # Initialize a dataframe with the first file
    merged_data = pd.read_csv(os.path.join(directory, csv_files.pop()))

    # Loop over the list of csv files
    for csv_file in csv_files:
        # Read each csv file into a DataFrame
        df = pd.read_csv(os.path.join(directory, csv_file))
            
        # Loop through the columns
        for column in df.columns:
            # We already got the activity_minute/date and id from the first file 
            # so we filter them out from this file
            if not column == 'id' and not column == 'activity_minute' and not column == 'date':
                # Adding the data from this file to our merge data
                merged_data[column] = df[column]

    # Write the merged data to a new CSV file
    merged_data.to_csv(f'{directory}/minute_activity.csv', index=False)
    print("Done!")

def main():
    merge(DIRECTORY)

if __name__ == '__main__':
    main()