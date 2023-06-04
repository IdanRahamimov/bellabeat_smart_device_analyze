# This sctipt was made to separate date and time to two columns 

import os
import pandas as pd
import dateutil
from datetime import time

# Specify the directory
DIRECTORY = "../data_april12_to_may12_2016"

def split_date_and_time(directory):
    # Loop through each CSV file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            print('working on:',filepath)
            # Load the file into a DataFrame
            df = pd.read_csv(filepath)

            # Loop through each column to find the datetime column
            for column in df.columns:
                # Try to parse the first value in the column into a datetime
                try:
                    dateutil.parser.parse(str(df[column][0]))
                    
                    # If the parsing is successful, this is likely the datetime column
                    # Copy the datetime column and drop then it 
                    datetime = pd.to_datetime(df[column]).copy()
                    df = df.drop(column, axis=1)

                    # Insert the date in the second column
                    df.insert(1,'date',datetime.dt.date)
                    # Insert the time in the third column if time was specified
                    if not datetime.dt.time[0] == time(0, 0, 0) or not datetime.dt.time[1] == time(0, 0, 0):
                        df.insert(2,'time',datetime.dt.time)
                    # Save the DataFrame back to a CSV file
                    df.to_csv(filepath, index=False)

                    # No need to check the other columns
                    break
                except ValueError:
                    # If the parsing fails, this is not a datetime column, so continue to the next one
                    continue

def main():
    print("This script can take couple of minutes depending on the amount of files and their size")
    # Call the function on the desired directory
    split_date_and_time(DIRECTORY)
    print("Done!")

if __name__ == '__main__':
    main()