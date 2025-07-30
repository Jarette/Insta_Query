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


def get_columns(df:pd.DataFrame) -> tuple[list:str,list:str]:
    original_column_names= df.columns.to_list()
    formated_column_names = []
    for column in original_column_names:
        new_name = column.lower()
        formated_column_names.append(new_name)
    return original_column_names,formated_column_names


df = read_dataframe(test_path)
og_cnames,new_cnames = get_columns(df)
print(new_cnames)
    