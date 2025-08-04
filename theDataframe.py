import pandas as pd
import pandas.api.types as pdtype
from getFile import get_file_extension
from tabulate import tabulate
import re

test_path = "C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

# path for at work "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx"

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

"""
Name: updating_columns
Description: updating the names of the columns in the data frame using the new list of formated column names
"""
def updating_columns(df:pd.DataFrame,orginal_names:list,new_names:list):
    
    # going through each column and renaming accorindingly 
    for original_name,new_name in zip(orginal_names,new_names):
        df.rename(columns={original_name:new_name}, inplace=True)

"""
Name: column_data_type
Description: gets the data type of the column passed in. List of data types below 

int64/32/16/8
uint64/32/16/8
float64/32/16
bool
object(this includes strings)
datetime64
Timedelta
"""
def column_data_type(df:pd.DataFrame,column:str):
    if pdtype.is_integer_dtype(df[column]):
        return "int"
    elif pdtype.is_float_dtype(df[column]):
        return "float"
    elif pdtype.is_datetime64_any_dtype(df[column]) or pdtype.is_datetime64_ns_dtype(df[column]) or pdtype.is_timedelta64_dtype(df[column]):
        return "time"
    elif pdtype.is_bool_dtype(df[column]):
        return "bool"
    elif pdtype.is_string_dtype(df[column]) or pdtype.is_object_dtype(df[column]):
        return "string"
    else:
        return "misc"

#df = read_dataframe(test_path)
#og_cnames,new_cnames = get_columns(df)
#updating_columns(df,og_cnames,new_cnames)
#for column in new_cnames:
 #   print(f"{column}: {column_data_type(df,column)}")
    