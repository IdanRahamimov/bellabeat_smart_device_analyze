#This sctipt made to change the file names to be snake_case style

import os
import re

def rename_files_in_dir(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            # Split the filename into parts: name and extension
            name, ext = os.path.splitext(filename)
            # Split the name part of the filename by capital letters
            parts = [part.lower() for part in re.split('([A-Z][^A-Z]*)', name) if part]
            # Join the parts with underscores
            new_name = '_'.join(parts) + ext
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    print("Done!")

def main():
    # Call the function on the desired directory
    rename_files_in_dir('../data_april12_to_may12_2016')

if __name__ == '__main__':
    main()