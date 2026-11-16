# About the Project

This project focuses on exploring and analysing the Airbnb Listings 2024 dataset using Python. The main objective was to understand how different factors, such as location, room type, pricing, availability, and customer reviews, relate to Airbnb listings.

I worked through the dataset step by step, starting with basic exploration and cleaning, followed by analysis and visualisation to identify patterns and relationships within the data.

##### Tools & Libraries Used

Python – Main programming language.

Pandas – Data loading, cleaning, manipulation, and analysis.

NumPy – Numerical operations.

Matplotlib – Creating charts and visualisations.

Seaborn – Statistical visualisation and exploring relationships between variables.

### Project Workflow

1. Importing Libraries

Imported the required Python libraries for data manipulation, numerical operations, and visualisation.

2. Loading the Dataset

Loaded the Airbnb listings dataset using Pandas and handled encoding issues while reading the CSV file.

3. Initial Data Exploration

Explored the dataset to understand its structure and contents.

Used info() to check column names, data types, and non-null values.

Used describe() to get a statistical summary of numerical columns.

4. Data Cleaning

Prepared the dataset for analysis by performing the following operations:

Checked for missing values.

Removed rows containing null values.

Identified and removed duplicate records.

Checked column data types.

Converted the id column into string format.

Filtered out listings with prices above 1,500 to reduce the impact of extreme price values.

5. Exploratory Data Analysis (EDA)

Performed both univariate and bivariate analysis to understand the dataset better.

Univariate Analysis

Used boxplots to examine price distribution and identify potential outliers.

Created a histogram to understand listing availability throughout the year.

Compared average prices across different neighbourhood groups.

Feature Engineering

Created a new column called price per bed.

Calculated it by dividing the listing price by the number of beds.

Used this feature to explore pricing in relation to accommodation capacity.

Bivariate Analysis

Examined how listing prices vary across neighbourhood groups and room types.

Used scatter plots to investigate the relationship between the number of reviews and listing prices.

Created pairplots to explore relationships between price, minimum nights, reviews, and availability.

Visualised the geographical distribution of Airbnb listings using latitude and longitude.

Generated a correlation matrix and heatmap to examine relationships between numerical variables.

### Key Analysis Areas

The project mainly explores the following questions:

How are Airbnb listing prices distributed?

How does availability vary across the year?

How do average prices differ between neighbourhood groups?

Does room type influence listing prices?

Is there any relationship between listing prices and the number of reviews?

How are Airbnb listings distributed geographically?

Which numerical variables have stronger correlations with each other?

How does pricing vary in relation to the number of beds?

### What I Learned:

While working on this project, I got practical experience with:

Loading and inspecting real-world CSV datasets.

Identifying and handling missing and duplicate records.

Working with Pandas DataFrames.

Filtering data and converting column data types.

Creating new features through feature engineering.

Performing univariate and bivariate analysis.

Using different visualisation techniques to understand data patterns.

Analysing correlations between numerical variables.

Project Structure

Airbnb-EDA/
│
├── datasets.csv
├── Airbnb_EDA.ipynb
└── README.md

#### Conclusion

This project helped me understand how to approach a real-world dataset, clean it, and explore it using Python. It also gave me hands-on experience with different visualisation techniques and helped me understand how data analysis can reveal patterns that are not immediately obvious from raw data.

The focus was on learning the complete EDA process, from loading a dataset to interpreting visual patterns and relationships.