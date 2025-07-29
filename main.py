import pandas as pd
from pandasql import sqldf
from tabulate import tabulate
import os

def SELECT(columns: list):
    Still_Choosing = True
    n = 0
    Select_choices = " "
    total_columns = len(columns)
    while Still_Choosing:
        if len(columns) == 0:
            return Select_choices
        else:
            for column in columns:
                n = n+1
                print(f"{n}. {column}")
            print(f"{len(columns)+1}. All")
            print(f"0. Finished selections")
            index = int(input("Enter the number coresponding with the column you would like as apart of your query: "))
            if index is len(columns)+1:
                return '*'
            else:
                if index == 0:
                    return Select_choices
                else:
                    choice = columns[index - 1]
                    if len(columns) < total_columns:
                        Select_choices = Select_choices + ',' + choice + ' '
                    else:
                        Select_choices = Select_choices + choice+ ' '
                    columns.pop(index-1)
                    n = 0
                    os.system('clear')
def WHERE(columns: list):
    n = 0
    total_columns = len(columns)
    Select_choices = " "
    while True:
        if len(columns) == 0:
            return Select_choices
        else:
            for column in columns:
                n = n+1
                print(f"{n}. {column}")
            print(f"0. Finished selections")
            index = int(input("Enter the number coresponding with the column you would like as apart of your query: "))
            choice = columns[index - 1]
            
pysqldf = lambda q: sqldf(q, locals())              
extension = ".xlsx"
query = ""
file_name = input("Enter the name of file you would like to use: ")
os.system('clear')
file_w_extension = file_name + extension
df = pd.read_excel(file_w_extension)
column_names= df.columns.to_list()
command_selection = """
Please Select the statements you would like to use
1. WHERE
2. WHERE, ORDER BY 
3. WHERE, ORDER BY, LIMIT
4. None
"""
print(command_selection)
command = int(input("Please select the number to correspond with the command order: "))
Select = SELECT(column_names)
Select_statement = f"SELECT{Select}"
os.system('clear')
query = Select_statement+"FROM df"
print(query)
result = sqldf(query)
print(tabulate(result, headers = 'keys', tablefmt = 'psql'))

# query = "SELECT id FROM df"
# result = sqldf(query)
#print(tabulate(df, headers = 'keys', tablefmt = 'psql'))