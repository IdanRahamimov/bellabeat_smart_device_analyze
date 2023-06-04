# Data Analysis Case Study: Smart Usage of Bellabeat Devices
This repository contains a case study project conducted for educational purposes, Please note that this project is independent and I am not affiliated with Bellabeat.


## About Bellabeat
Bellabeat is a company that produces health-focused smart devices for women. With a mission to empower women by providing insights about their health and habits, Bellabeat has become a major player in the women's wellness tech market.

## Project Objective
The aim of this project is to uncover insights into how consumers are using Bellabeat's smart devices. The goal is to inform and enhance the company's marketing strategy by providing data-driven recommendations.

## Methodology
The project follows the Ask, Prepare, Process, Analyze, Share, and Act (APPASA) framework for data analysis.

## Data Transformation Process
This section outlines the process of transforming and organizing the data for analysis. The cleaned and prepared data can be found in the `data_april12_to_may12_2016` folder which will be the basis for the ensuing analysis.

  ### Steps:
  1. **Conversion to Snake_case**: To maintain consistency and compatibility, all filenames and headers were converted to snake_case. This was done using the `rename_file_name.py` script located in the `scripts` folder. Then, the `rename_header.py` script was employed for renaming the headers within the data files.

  2. **Removal of Duplicate Data**: The `daily_activity` dataset contains comprehensive daily data; hence, the `daily_calories`, `daily_intensities`, and `daily_steps` datasets, which held redundant information, were removed.

  3. **Data Merging**: The data divided into hourly and minute intervals were consolidated for ease of analysis. The hourly data was manually combined into a `hourly_activity` dataset.
  The minute data, due to its voluminous size, required the `merge_minute.py` script for consolidation into a single `minute_activity` file. Prior to running the script, the `minute_sleep` dataset was renamed to `time_sleep` to prevent it from being merged.
  
  4. **Date and Time Separation**: Some of the datasets included date and time in the same column. The `split_datetime.py` script was created to separate these into distinct 'date' and 'time' columns. This script also standardizes the column names across all datasets.

## Source
[Kaggle FitBit Fitness Tracker](https://www.kaggle.com/datasets/arashnic/fitbit)
