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

## Data Analysis Process

After transforming and cleaning the data, I started the analysis phase. Here are the steps I followed:

  1. **Excel Integration**: I imported my dataset into an Excel workbook using Power Query.

  2. **Correlation Analysis**: I used Excel's `CORREL` function to calculate the correlation between different metrics. This helped to identify which variables had a strong relationship.

  3. **Derived Fields**: Using averages, sums, and arithmetic, I derived new metrics from the original data.

  4. **Data Aggregation**: I used pivot tables and the `VLOOKUP` function to aggregate data and create new derived metrics. This was necessary for analysing data from different sources and for summarizing the data in meaningful ways.

  5. **Data Visualization**: I created some charts and tables to visualize the data and the relationships between different metrics.

### Key Findings
- High-intensity, short-duration exercises are more effective in burning calories compared to lower-intensity exercises performed over a longer duration.

- Running burns approximately 118 calories per mile. However, daily activities alone can burn around 1650 calories, indicating that everyday movement is significant for calorie loss, sometimes matching the calorie loss from dedicated running sessions.

### Conclusions and Recommendations
Our analysis highlights that the human body consistently burns calories, even in the absence of dedicated exercise. However, engaging in physical exercise amplifies this calorie burn, with the rate and efficiency increasing with exercise intensity. Therefore, we recommend that Bellabeat users incorporate high-intensity exercises into their routine for optimal calorie burn. Bellabeat could also consider incorporating features into their smart devices that provide insights on how to increase this intensity for a more efficient calorie burn.

## Source
[Kaggle FitBit Fitness Tracker](https://www.kaggle.com/datasets/arashnic/fitbit)
