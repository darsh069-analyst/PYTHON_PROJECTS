"""

"""
 
#Importing all the required dependencies

import pandas as pd
import os

#Function to clean the dataframe

def Dataframe_cleaner(data_path, data_name, script_directory):
    
    #Checking if the file exists

        if not os.path.isfile(data_path):
            print("The specified path does not exist.")
            print("Please check the path and try again.")            
            return
        
        else:

            #Checking if the file type is supported or not
            if data_path.endswith('.csv'):
                print("The file is a CSV file. \nProceeding with cleaning.")
                data = pd.read_csv(data_path)

            elif data_path.endswith('.xlsx'):
                print("The file is an Excel file. \nProceeding with cleaning.")
                data = pd.read_excel(data_path)
            
            else:
                print("The file type is not supported.")
                print("Please provide a CSV or Excel file.")
                
                return

        #Showing number of records in the datarframe
        print(f"Total number of rows in the dataframe is: {data.shape[0]}" 
              f"\nTotal number of columns in the dataframe is: {data.shape[1]}")

        #Starting to clean the dataframe by removing any duplicate records
        duplicates = data.duplicated()
        total_duplicates = data.duplicated().sum()
        print(f"Total number of duplicate rows in the dataframe is: "
              f"{total_duplicates}")
        
        #Creating a new dataframe with only the duplicate records
        if total_duplicates > 0:
            duplicate_records = data[duplicates] 
            duplicate_records.to_csv(f'{data_name}_duplicates.csv', index=None)

        #Deleting the duplicate records from the original dataframe
        df = data.drop_duplicates().copy()

        #Find missing values in the dataframe
        Total_missing_values = df.isnull().sum().sum()
        missing_values_columns = df.isnull().sum()

        print(
                f"Total number of missing values in the dataframe is: "
                f"{Total_missing_values}"
            )
        
        print(f"Missing values in each column:\n{missing_values_columns}")

        #Dealing with missing values:

        columns = df.columns

        for col in columns:
        
        #Filling the missing values in the column with the mean of the column if the column is of type float or int
        
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(df[col].mean())
            
            else:
        
        #Dropping the rows with missing values in the column
        
                df.dropna(subset=[col], inplace=True)

        #Saving the cleaned dataframe to a new CSV file
        print("\nData cleaning is complete. \u2713")
        
        print(
                "Number of rows in the cleaned dataframe is:",
                df.shape[0]
            )
        print(
                "Number of columns in the cleaned dataframe is:",
                df.shape[1]
            )
        
        #Saving the cleaned dataframe to a new CSV file
        output_file = os.path.join(
            script_directory,
                f'{data_name}_cleaned.csv'
            )
        df.to_csv(output_file, index=False)
        
        print(f"Cleaned dataframe is saved to: {output_file}")
        
        return df

#Main function to run the script
if __name__ == "__main__":

    print(
        "Welcome to the Dataframe Cleaner!\n"
        "This tool will help you clean your dataframe by "
        "removing duplicate records and handling missing values."
    )

#Getting the directory where the Python script is saved

    script_directory = os.path.dirname(os.path.abspath(__file__))  
    #Asking the user to input the name of the file

    data_name = input(
        "\nPlease enter the name of the output file (without extension): "
    ).strip()

    file_name = input(
        "Please enter the file name (e.g. sales.csv): "
    ).strip().strip('"')

#Constructing the complete file path

    data_path = os.path.join(script_directory, file_name)


#Displaying the file path

    print(f"\nChecking file location: {data_path}")


#Cleaning the dataframe by calling the function

    Dataframe_cleaner(data_path, data_name)
