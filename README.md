# Data Analysis Case Study: Smart Usage of Bellabeat Devices
This repository contains a case study project conducted for educational purposes, Please note that this project is independent and I am not affiliated with Bellabeat.


## About Bellabeat
Bellabeat is a company that produces health-focused smart devices for women. With a mission to empower women by providing insights about their health and habits, Bellabeat has become a major player in the women's wellness tech market.

## Project Objective
The aim of this project is to uncover insights into how consumers are using Bellabeat's smart devices. The goal is to inform and enhance the company's marketing strategy by providing data-driven recommendations.

## Methodology
The project follows the Ask, Prepare, Process, Analyze, Share, and Act (APPASA) framework for data analysis.

## Data Transformation Process
This section outlines the process of transforming and organizing the data for analysis. The cleaned and prepared data can be found in the `data_april12_to_may12_2016` folder. This dataset will be used for subsequent analysis.

  ### Steps:
  1. **Conversion to Snake_case**: To maintain consistency and compatibility, all file names and headers have been converted to snake_case. This conversion was achieved using the `rename_file_name.py` script found   in the `scripts` folder. Then, the `rename_header.py` script was used to convert the headers within the data files.
  2. **Delete duplicate data**: `daily_activity` already hold all the daily information so I delete `daily_calories`, `daily_intensities` and `daily_steps`
  3. **Merge Data**: the hourly and minute data are separated so I manually combine the hourly data to `hourly_activiy`, the data in minute was too large to merge manually so I made `merge_minute.py` script to merge them all into one file calld `minute_activity`
## Source
[Kaggle FitBit Fitness Tracker](https://www.kaggle.com/datasets/arashnic/fitbit)
