import pandas as pd
import pandasql as pdsql
from theDataframe import read_dataframe
import tkinter as tk
from tkinter import ttk

test_path = "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx"

#"C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

# path for at work "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx"

"""
Name: collect_column

Description: This function collects the name of the button pressed corresponding to the 
column being selected by the user and stores the list of columns selected and changes the 
column blue if selected. If a column is selected twice it does update the list
"""
def collect_columns(column_name:str, column_widget:tk.Button, selected_columns:list):
    # changing color of button to blue 
    column_widget.config(bg="blue")
    
    # making sure there is no duplicate
    if column_name not in selected_columns:
        selected_columns.append(column_name)


"""
Name: column_selection
Description: This function opens a window to show buttons with the names of the columns to use 
for collecting the colunms selected by the user and once finished can click next to move on to the 
next part of the query
"""
def column_selection(original_column_names:list,formated_column_names,selected_columns:list):
    
    # create the window 
    window = tk.Tk()
    window.title("Select Columns")
    
    # empty list to store buttons 
    buttons = []
    
    # generate the buttons based on how much columns are in the dataframe 
    for i,(og_columns,new_columns) in enumerate(zip(original_column_names,formated_column_names)):
        button = tk.Button(window,text = og_columns)
        button.configure(command= lambda nc=new_columns, b=button: collect_columns(nc,b,selected_columns))
        button.grid(row=i, column=0, padx=10, pady=5)
        buttons.append(button)
    
    # the button to close the window and move unto the next step 
    close_button = ttk.Button(window, text="Next", command=window.destroy)
    close_button.grid(row=len(original_column_names), column=0, pady=10)
    
    # generating the window width to ensure title shows 
    window.update_idletasks()
    current_height = window.winfo_height()
    window.geometry(f"500x{current_height}")
    
    
    window.mainloop()

"""
Name: column_selection
Description: takes the list of selected columns and generate a SQL SELECT statement using those column
in correct syntax
"""

def SELECT_statemet(selected_columns:list):
    # base SELECT statement 
    select_statement = "SELECT "

    # if there is only one element remaining add it to statement but no comma 
    for columns in selected_columns:
        if len(selected_columns) == 1:
            select_statement = select_statement + f"{columns} "
        else: 
            # adding the comma if there is expected atleast one more element to be added 
            select_statement = select_statement + f"{columns}, "

            # removing the column after beinng used 
            selected_columns.remove(columns)
    return select_statement

def get_selected_choice(choices:list[tk.StringVar],final_choices:list):
    for choice in choices:
        final_choices.append(choice.get())

def ascending_or_descending(selected_columns:list):
    window = tk.Tk()
    window.title("ASC or DESC")
    options = ["ASC","DESC"]
    choices = []
    menus = []
    labels = []
    ASC_or_DESC = []
    
    for i,columns in enumerate(selected_columns):
        label = tk.Label(window, text = columns)
        label.grid(row=i, column=0, padx=10, pady=5)
        labels.append(label)

        selected_choice = tk.StringVar(window)
        selected_choice.set(options[0])
        choices.append(selected_choice)

        option_menu = tk.OptionMenu(window,selected_choice,*options)
        option_menu.grid(row=i, column=2, padx=10, pady=5)
        menus.append(option_menu)

    finalize_button = tk.Button(window, text="Finalize choices", command= lambda : get_selected_choice(choices, ASC_or_DESC))
    finalize_button.grid(row=len(selected_columns), column=0, pady=10)

    close_button = ttk.Button(window, text="Next", command=window.destroy)
    close_button.grid(row=len(selected_columns)+1, column=0, pady=10)

    window.update_idletasks()
    current_height = window.winfo_height()
    window.geometry(f"500x{current_height}")
    window.mainloop()
    return ASC_or_DESC

def ORDER_BY_statement(selected_columns:list, ascending_or_descending:list):
    order_by_statement = "ORDER BY "
    combine 
    for colunms in selected_columns:
        print(colunms)
    return order_by_statement

   



selected_columns = []
finalize_selections = []
df = read_dataframe(test_path)
column_names = df.columns.to_list()
column_selection(column_names,column_names,selected_columns)
finalize_selections = ascending_or_descending(selected_columns)
print(selected_columns)
print(finalize_selections)
print(ORDER_BY_statement(selected_columns,finalize_selections))

