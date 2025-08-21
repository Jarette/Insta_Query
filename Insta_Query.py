import pandas as pd
from pandasql import sqldf
from tabulate import tabulate
import os

from getFile import validating_file
from getFile import get_file_extension
from theDataframe import *

from TheSQL import column_selection
from TheSQL import column_selection_w_all
from TheSQL import SELECT_statement
from TheSQL import statement_selection
from TheSQL import WHERE_statement
from TheSQL import generate_WHERE_statement
from TheSQL import ascending_or_descending
from TheSQL import ORDER_BY_statement
from TheSQL import LIMIT_statement
from TheSQL import generate_query

from generateOutput import perform_query
from generateOutput import output_window

where = ""
order_by =""
limit =""

#Step 1 ask user for csv or xlsx file and save the dataframe 
path = validating_file()
if get_file_extension(path) == ".csv":
    df = read_dataframe(path)
else:
    dfs = read_dataframe(path)
    df = select_table(dfs)

# Step 2 have user select columns 

original_names, formated_names = get_columns(df)
updating_columns(df,original_names,formated_names)

selected_columns1 = []
og_selected_columns1 = []

column_selection_w_all(original_names,formated_names,selected_columns1,og_selected_columns1)

# Step 3 generate the SELECT STATEMENT

select = SELECT_statement(selected_columns1,original_names) + " "

# Step 4 Ask the user if they would like add a WHERE statement

where_choice = statement_selection("WHERE STATEMENT", "Would you like to add a Where Statement")

# if yes generate the where stament 
if where_choice is True:
    
    selected_columns = []
    og_selected_columns = []
    
    column_selection(original_names,formated_names,selected_columns,og_selected_columns)
    
    Where_info = WHERE_statement(df,selected_columns,og_selected_columns)
    
    where = generate_WHERE_statement(selected_columns,Where_info)
    
# Step 5 Ask user if they would like an order by statement 

order_choice = statement_selection("ORDER BY STATEMENT", "Would you like to add an ORDER BY statement?")

#if yes generate order by statement
if order_choice is True:
    
    selected_columns.clear()
    og_selected_columns.clear()
    
    column_selection(original_names,formated_names,selected_columns,og_selected_columns)   
    
    the_orders = ascending_or_descending(selected_columns)
    
    order_by = ORDER_BY_statement(selected_columns,the_orders)
    

# Step 6 Ask the user if they would like a limit statement 

limit_choice = statement_selection("LIMIT STATEMENT", "Would you like to addd a LIMIT statment?")

# if yes generate LIMIT Statement
if limit_choice is True:
    
    limit = LIMIT_statement()
    

# Step 7 generate the query 

query = generate_query(select,where,order_by,limit)

# Step 8 Perform the query 

result = perform_query(df,query)

# Step 9 Distplay the results and ask the user if they would like to save the results

output_window("YOUR RESULTS", result, og_selected_columns1, selected_columns1)



    
    







