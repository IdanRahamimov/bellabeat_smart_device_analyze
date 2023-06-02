# This script was made to change the header of the csv file from camel case to snake case

import os
import re
import pandas as pd

# Specify the directory
DIRECTORY = "../data_april12_to_may12_2016"

# Define function to convert camel case to snake case
def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def rename_header_in_dir(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)

            # Load the CSV file
            df = pd.read_csv(file_path)

            # Convert column headers to snake case
            df.columns = [camel_to_snake(col) for col in df.columns]

            # Save the DataFrame back to CSV
            df.to_csv(file_path, index=False)

def main():
    # Call the function on the desired directory
    rename_header_in_dir(DIRECTORY)
    print("Done!")
    
if __name__ == '__main__':
    main()
