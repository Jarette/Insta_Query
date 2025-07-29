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
            os.system('clear')
            choice = columns[index - 1]
            Select_choices = Select_choices + choice + " "
            columns.pop(index-1)
            condition = input("Please enter the condition of the Where: ")
            os.system('clear')
            Select_choices = Select_choices + condition + " "
            print("Would you like to add another WHERE condition and if so would you like AND or OR?")
            print("1. AND")
            print("2. OR")
            print("3. None")
            extension = int(input("Enter choice: "))
            os.system('clear')
            if extension == 1: 
                Select_choices = Select_choices + 'AND' + " "
                n = 0
            elif extension == 2:
                Select_choices = Select_choices + 'OR' + " "
                n = 0
            else:
                return Select_choices
def ORDERBY(columns: list):
    n = 0
    Select_choices = " "
    total_columns = len(columns)
    while True:
        if len(columns) == 0:
            return Select_choices
        else:
            for column in columns:
                n = n+1
                print(f"{n}. {column}")
            print(f"0. Finished selections")
            index = int(input("Enter the number coresponding with the column you would like as apart of your query: "))
            os.system('clear')
            if index == 0:
                return Select_choices
            else:
                choice = columns[index - 1]
                if len(columns) < total_columns:
                    order = int(input("Would you like 1. Ascending or 2.Descending"))
                    if order == 1:
                        Select_choices = Select_choices + ',' + choice + ' ' + 'ASC' + ' '
                    else: 
                         Select_choices = Select_choices + ',' + choice + ' ' + 'DESC' + ' '
                else:
                    order = int(input("Would you like 1. Ascending or 2.Descending"))
                    if order == 1:
                        Select_choices = Select_choices + choice + ' ' + 'ASC' + ' '
                    else: 
                         Select_choices = Select_choices + choice + ' ' + 'DESC' + ' '
                columns.pop(index - 1)
                n = 0
                os.system('clear')
                
                
                
            
                  
pysqldf = lambda q: sqldf(q, locals())              
extension = ".xlsx"
query = ""
file_name = input("Enter the name of file you would like to use: ")
os.system('clear')
file_w_extension = file_name + extension
df = pd.read_excel(file_w_extension)
column_names= df.columns.to_list()
Where = WHERE(column_names)
print(Where)
#Select = SELECT(column_names)
#Select_statement = f"SELECT{Select}"
#os.system('clear')
#query = Select_statement+"FROM df"
#print(query)
#result = sqldf(query)
#print(tabulate(result, headers = 'keys', tablefmt = 'psql'))

# query = "SELECT id FROM df"
# result = sqldf(query)
#print(tabulate(df, headers = 'keys', tablefmt = 'psql'))