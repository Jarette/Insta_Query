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
                    os.system('cls')
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
            os.system('cls')
            choice = columns[index - 1]
            Select_choices = Select_choices + choice + " "
            columns.pop(index-1)
            condition = input("Please enter the condition of the Where: ")
            os.system('cls')
            Select_choices = Select_choices + condition + " "
            print("Would you like to add another WHERE condition and if so would you like AND or OR?")
            print("1. AND")
            print("2. OR")
            print("3. None")
            extension = int(input("Enter choice: "))
            os.system('cls')
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
            os.system('cls')
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
                os.system('cls')

def LIMIT(): 
    limit = int(input("Please enter how much you data points you would like to see: "))
    os.system('cls')
    choice = int(input("Would you like to add an offset 1.Yes or 2.No"))
    if choice == 1:
        os.system('cls')
        offset = int(input("please enter the offset: "))
        os.system('cls')
        return f"{limit} OFFSET {offset}" 
    else:
        os.system('cls')
        return f"{limit}"

## MAIN DRIVER
           
pysqldf = lambda q: sqldf(q, locals())              
extension = ".xlsx"
query = ""
file_name = input("Enter the name of file you would like to use: ")
os.system('cls')
file_w_extension = file_name + extension
df = pd.read_excel(file_w_extension)
column_names= df.columns.to_list()
limit = LIMIT()
print(limit)
#Select = SELECT(column_names)
#Select_statement = f"SELECT{Select}"
#os.system('cls')
#query = Select_statement+"FROM df"
#print(query)
#result = sqldf(query)
#print(tabulate(result, headers = 'keys', tablefmt = 'psql'))

# query = "SELECT id FROM df"
# result = sqldf(query)
#print(tabulate(df, headers = 'keys', tablefmt = 'psql'))