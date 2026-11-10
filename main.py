#Importing required dependencies

import os

#Importing the Dataframe_cleaner function
from Dataframe_cleaner import Dataframe_cleaner

#Getting the current script directory

script_directory = os.path.dirname(os.path.abspath(__file__))

#Taking input from the user

file_name = input("Enter the file name (e.g. sales.csv): ")

data_name = input("Enter the output file name: ")

#Creating the complete file path

data_path = os.path.join(script_directory, file_name)

#Calling the imported function

Dataframe_cleaner(data_path, data_name, script_directory)