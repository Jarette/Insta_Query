import pandas as pd
from getFile import get_file_extension
import tabulate as tabulate

test_path = "C:\Users\jgreene\Desktop\Insta_Query\Insta_Query\Test.xlsx"

"""
Name: read_dataframe
Description: Reads a DataFrame from a file, which can be either an Excel or CSV file
"""
def read_dataframe(test_path: str) -> pd.DataFrame:

    # Get the file extension
    ext = get_file_extension(test_path)

    # Read the file based on its extension
    if ext == 'xlsx':
        # reading the excel file 
        df = pd.read_excel(test_path)
    elif ext == 'csv':
        # reading the csv file
        df = pd.read_csv(test_path)
    else:
        # error checking message
        raise ValueError(f"Unsupported file extension: {ext}")
    
    # returning the dataframe
    return df

def get_columns(df:pd.DataFrame) -> tuple[list:str,list:str]:
    return 0

    