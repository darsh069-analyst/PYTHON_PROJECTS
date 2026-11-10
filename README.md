# DataFrame Cleaner

A Python-based data cleaning tool built using **Pandas** that automates basic data preprocessing tasks. It allows users to clean CSV and Excel datasets by identifying and removing duplicate records, detecting missing values, and handling missing data.

The tool exports the cleaned dataset into a new CSV file while preserving the original dataset.

## Features
- **CSV & Excel Support:** Reads datasets in `.csv` and `.xlsx` formats.
- **File Validation:** Checks whether the specified file exists and verifies its format.
- **Dataset Overview:** Displays the total number of rows and columns.
- **Duplicate Detection:** Identifies duplicate records and displays their count.
- **Duplicate Export:** Saves duplicate records separately into a CSV file.
- **Duplicate Removal:** Removes duplicate records from the original dataset.
- **Missing Value Detection:** Identifies and calculates missing values across all columns.
- **Missing Value Handling:**
  - Numerical columns: Replaces missing values with the column mean.
  - Non-numerical columns: Removes rows containing missing values.
- **Cleaned Dataset Export:** Saves the cleaned dataset into a new CSV file.

## Technologies Used
- Python
- Pandas
- OS Module

## Project Structure
```text
DataFrame-Cleaner/
│
├── dataframe_cleaner.py
├── main.py
├── sales.csv
├── sales_duplicates.csv
├── sales_cleaned.csv
└── README.md
```

**File Description:**

- `dataframe_cleaner.py` – Contains the main data cleaning function.
- `main.py` – Imports and executes the data cleaning function.
- `sales.csv` – Sample input dataset.
- `sales_duplicates.csv` – Exported duplicate records.
- `sales_cleaned.csv` – Final cleaned dataset.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/darsh069-analyst/DataFrame-Cleaner.git
```

### 2. Navigate to the Project Directory

```bash
cd DataFrame-Cleaner
```

### 3. Install Dependencies

```bash
pip install pandas openpyxl
```

## How to Use

### Method 1: Run the Main File
Execute the following command in your terminal:

```bash
python main.py
```

Enter the required information when prompted:

```text
Enter the file name: sales.csv

Enter the output file name: sales
```

The program will automatically locate the input file in the project directory and begin cleaning.

### Method 2: Import as a Function
You can also import the cleaning function into another Python script.

```python
import os

from dataframe_cleaner import Dataframe_cleaner

script_directory = os.path.dirname(os.path.abspath(__file__))

file_name = "sales.csv"
data_name = "sales"

data_path = os.path.join(script_directory, file_name)

Dataframe_cleaner(data_path, data_name, script_directory)
```

This allows the cleaning functionality to be reused in other Python projects without duplicating the code.

## Output Files
The program generates the following files:

| Output File            | Description                                                    |
| ---------------------- | -------------------------------------------------------------- |
| `sales_duplicates.csv` | Contains duplicate records identified in the original dataset. |
| `sales_cleaned.csv`    | Contains the final cleaned dataset.                            |

*Note: The duplicate file is generated only when duplicate records are found.*

## Data Cleaning Workflow
The program follows these steps:
1. Accepts the input dataset.
2. Validates the file path and format.
3. Reads the dataset using Pandas.
4. Displays the initial dataset dimensions.
5. Identifies duplicate records.
6. Exports duplicate records separately.
7. Removes duplicate records.
8. Identifies missing values in each column.
9. Fills numerical missing values using the column mean.
10. Drops rows containing missing values in non-numerical columns.
11. Displays the final dataset dimensions.
12. Exports the cleaned dataset as a CSV file.

## Limitations
- Currently supports only CSV and XLSX files.
- Numerical missing values are handled using the mean method.
- Rows containing missing categorical values are removed.
- Does not currently perform outlier detection or data type correction.
- Requires the input dataset to be accessible from the project directory when using `main.py`.

## Future Improvements
- [ ] Add median and mode imputation.
- [ ] Implement outlier detection using the IQR method.
- [ ] Add automatic data type correction.
- [ ] Standardise column names.
- [ ] Handle empty columns.
- [ ] Generate a detailed data cleaning report.
- [ ] Add data visualisation before and after cleaning.
- [ ] Support additional file formats.

## Learning Outcomes
Through this project, I practised:
- Working with Pandas DataFrames.
- Handling missing and duplicate data.
- Reading and exporting CSV and Excel files.
- Python functions and parameter passing.
- Importing reusable functions across Python modules.
- File handling using Python's OS module.
- Building modular and reusable Python scripts.

## Author

**Adarsh Mahakuda**

Aspiring Data Analyst | Python | SQL | Excel | Data Analytics

---

If you find this project useful, consider giving the repository a star!
