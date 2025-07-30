import pandas as pd
from getFile import get_file_extension
from tabulate import tabulate
import re

test_path = "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx"

"""
Name: read_dataframe
Description: Reads a DataFrame from a file, which can be either an Excel or CSV file
"""
def read_dataframe(test_path: str) -> pd.DataFrame:

    # Get the file extension
    ext = get_file_extension(test_path)

    # Read the file based on its extension
    if ext == '.xlsx':
        # reading the excel file 
        df = pd.read_excel(test_path)
    elif ext == '.csv':
        # reading the csv file
        df = pd.read_csv(test_path)
    else:
        # error checking message
        raise ValueError(f"Unsupported file extension: {ext}")
    
    # returning the dataframe
    return df


"""
Name: get_columns
Description: Reads in a data frame and gets the name of the columns from the data frame
keeping the original names of the column and the new formated names removing spaces and all 
alphamuneric characters. Then return the both the list of string of original names and formated names 
"""
def get_columns(df:pd.DataFrame) -> tuple[list:str,list:str]:

    # getting the original names of the colunmns and saving them as a string 
    original_column_names= df.columns.to_list()

    # initializing list to store formated names 
    formated_column_names = []

    # going through each column name 
    for column in original_column_names:
        # making all names lower case
        new_name = column.lower()

        # removing all special characters and space
        new_name2 = re.sub(r"[^a-zA-Z0-9]",'',new_name)

        # saving this new name to a different list
        formated_column_names.append(new_name2)

    # returning the list of of original names and formated names respectively
    return original_column_names,formated_column_names

def updating_columns(df:pd.DataFrame) -> pd.DataFrame:
    
    return 0
df = read_dataframe(test_path)
og_cnames,new_cnames = get_columns(df)
print(new_cnames)
    