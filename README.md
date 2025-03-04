# Customer Transactions Data Cleaning

## 📌 Overview
This project is a **data preprocessing script** that reads a CSV file containing customer transaction data, handles missing values, removes duplicates, normalizes numerical columns, and saves the cleaned data to a new file.

## 🔍 Features
- **Handles Missing Values**:
  - Replaces missing values in numeric columns with the column mean.
  - Fills missing values in categorical columns with the most frequent value (mode).
- **Removes Duplicates**:
  - Drops duplicate records to ensure data integrity.
- **Normalizes Numeric Data**:
  - Scales numerical columns to a range between 0 and 1 using **min-max normalization**.
- **Exports Cleaned Data**:
  - Saves the cleaned dataset as `cleaned_data.csv`.

## 🛠 Technologies Used
- **Python**
- `pandas`
- `numpy`
