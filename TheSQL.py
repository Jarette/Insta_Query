import pandas as pd
import pandasql as pdsql
from theDataframe import column_data_type
from theDataframe import read_dataframe
import tkinter as tk
from tkinter import ttk

test_path = "C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

#"C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

# path for at work "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx"

"""
Name: collect_column

Description: This function collects the name of the button pressed corresponding to the 
column being selected by the user and stores the list of columns selected and changes the 
column blue if selected. If a column is selected twice it does update the list
"""
def collect_columns(column_name:str, column_widget:tk.Button, selected_columns:list, og_column_name:str, selected_og_columns:list):
    # changing color of button to blue 
    column_widget.config(bg="blue")
    
    # making sure there is no duplicate
    if column_name not in selected_columns:
        selected_columns.append(column_name)
        selected_og_columns.append(og_column_name)


"""
Name: column_selection
Description: This function opens a window to show buttons with the names of the columns to use 
for collecting the colunms selected by the user and once finished can click next to move on to the 
next part of the query
"""
def column_selection(original_column_names:list,formated_column_names,selected_columns:list,selected_og_columns:list):
    
    # create the window 
    window = tk.Tk()
    window.title("Select Columns")
    
    # empty list to store buttons 
    buttons = []
    
    # generate the buttons based on how much columns are in the dataframe 
    for i,(og_columns,new_columns) in enumerate(zip(original_column_names,formated_column_names)):
        button = tk.Button(window,text = og_columns)
        button.configure(command= lambda nc=new_columns, b=button, og=og_columns : collect_columns(nc,b,selected_columns,og,selected_og_columns))
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
def SELECT_statement(selected_columns: list):
    select_statement = "SELECT " + ", ".join(selected_columns)
    return select_statement

"""
Name: get_selected_choice
Description: collecting the user selecctions from the drop menu for picking ascending and descending order
"""
def get_selected_choice(choices:list[tk.StringVar],final_choices:list):
    for choice in choices:
        final_choices.append([choice.get()])

"""
Name: ascending_or_descending
Description: This function displays a window that allows the user to pick the order you would like to set for the dataframe
using a drop down menu selection.
"""
def ascending_or_descending(selected_columns:list):
    # the selection window 
    window = tk.Tk()
    window.title("ASC or DESC")
    options = ["ASC","DESC"]
    
    # necessary lists to store buttons and results
    choices = []
    menus = []
    labels = []
    ASC_or_DESC = []
    
    # generating buttons based on the number of columns selected
    for i,columns in enumerate(selected_columns):
        # placing the columns names
        label = tk.Label(window, text = columns)
        label.grid(row=i, column=0, padx=10, pady=5)
        labels.append(label)
        
        # creating the selection handler
        selected_choice = tk.StringVar(window)
        selected_choice.set(options[0])
        choices.append(selected_choice)

        # the drop down menu 
        option_menu = tk.OptionMenu(window,selected_choice,*options)
        option_menu.grid(row=i, column=2, padx=10, pady=5)
        menus.append(option_menu)

    # this button when clicks gathers all the selections 
    finalize_button = tk.Button(window, text="Finalize choices", command= lambda : get_selected_choice(choices, ASC_or_DESC))
    finalize_button.grid(row=len(selected_columns), column=0, pady=10)
    
    # button to close the window and move onto the next step
    close_button = ttk.Button(window, text="Next", command=window.destroy)
    close_button.grid(row=len(selected_columns)+1, column=0, pady=10)

    # ensuring the width is long enough to display window title 
    window.update_idletasks()
    current_height = window.winfo_height()
    window.geometry(f"500x{current_height}")
    window.mainloop()
    return ASC_or_DESC

"""
Name: ORDER_BY_statement 
Description: This function creates the ORDER BY statement for the final sql statement 
"""
def ORDER_BY_statement(selected_columns:list, ascending_or_descending:list):
    combine =list(zip(selected_columns,ascending_or_descending))
    order_by_part = [f"{col} {order}" for col,order in combine]
    order_by_statement = "ORDER BY " + ", ".join(order_by_part)
    return order_by_statement

"""
Name: get_input
Description: This function compiles the inputs entered by the users through a text box  
"""
def get_input(data:list, entry:list[tk.Entry]):
    for entries in entry:
        data.append(entries.get())

"""
Name: only_allow_integer
Description: This function ensures that the value being entered is an integer or a blank space   
"""
def only_allow_integers(new_value):
    if new_value == "" or new_value.isdigit():
        return True
    return False

"""
Name: LIMIT_statement
Description: This function will create a window to receive text data from the user for the SQL LIMIT and 
OFFSET statements making sure to recieve number inputs and returns an approipriately formated 
SQL LIMIT and OFFSET statements 
"""
def LIMIT_statement():
    # list storing the entries and the data collected 
    entries =[]
    data = []
    
    # created the window 
    window = tk.Tk()
    window.title("Limit and Offset Input")
    
    # the validation command used to ensure integers are entered
    vcmd = (window.register(only_allow_integers), "%P")
    
    # label for the first user entry point 
    label = tk.Label(window, text = "How many rows would you like displayed: ")
    label.grid(row=0, column=0, padx=10, pady=5)
    
    # First entry 
    entry = tk.Entry(window,width=50,validate="key",validatecommand=vcmd)
    entry.grid(row=0, column=1,padx=10, pady=5)
    entries.append(entry)
    
    # Second entry label 
    label = tk.Label(window, text = "Where would you like to start the data: ")
    label.grid(row=1, column=0, padx=10, pady=5)
    
    # second label
    entry2 = tk.Entry(window,width=50,validate="key",validatecommand=vcmd)
    entry2.grid(row=1, column=1,padx=10, pady=5)
    entries.append(entry2)
    
    # button to collect all the data points 
    finalize_button = tk.Button(window, text="Finalize choices", command= lambda : get_input(data,entries) )
    finalize_button.grid(row= 2, column=0, pady=10)
    
    # button to close the window 
    close_button = ttk.Button(window, text="Next", command=window.destroy)
    close_button.grid(row=3, column=0, pady=10)
    
    # Ensuring the window is wide enough to display the title 
    window.update_idletasks()
    current_height = window.winfo_height()
    window.geometry(f"500x{current_height}")
    window.mainloop()
    
    # casting the input to an integer
    intdata = [int(s) for s in data]
    
    # gennerating the limit statement 
    if intdata[1] <= 1:
        return f"LIMIT {data[0]} "
    else:
        return f"LIMIT {data[0]} OFFSET {data[1]} "

def gather_data_types(df:pd.DataFrame, selected_columns:list):
    data_types = []
    for col in selected_columns:
        data_types.append(column_data_type(df,col))
    return data_types

def get_selected_choice2(choices:list[tk.StringVar,int],final_choices:list):
    for choice in choices:
        if len(choice) == 4:
            if choice[0] == "time":
                final_choices.append([choice[1],choice[2].get(),choice[3].get()])
            else:
                final_choices.append([choice[2],choice[1].get(),choice[3].get()])
        elif len(choice) == 3:
            final_choices.append([choice[2],choice[1].get()]) 

def only_allow_numbers(new_value):
    if new_value == "":
        return True
    try:
        float(new_value)
        return True
    except ValueError:
        return False
        
def WHERE_statement(df:pd.DataFrame, selected_columns:list, og_column_names:list):
    data_types = gather_data_types(df,selected_columns)
    og_selected_datatypes = zip(og_column_names,selected_columns,data_types)
    conditionals = ["equal","not equal","less than", "less than or eqaul to", "greater than", "greater than or equal to"]
    booleans = ["True", "False"]
    string_options = ["Starts with", "Contains", "Ends with"]
    labels = []
    choices = []
    menus = []
    entries = []
    selected_condtionals = []
    window = tk.Tk()
    window.title("Limit and Offset Input")
    vcmd = (window.register(only_allow_integers), "%P")
    vcmd2 = (window.register(only_allow_numbers), "%P")
    
    for i,columns in enumerate(og_selected_datatypes):
        label = tk.Label(window, text = columns[0])
        label.grid(row=i, column=0, padx=10, pady=5)
        labels.append(label)
        
        if columns[2] == "int":
            selected_choice = tk.StringVar(window)
            selected_choice.set(conditionals[0])
            
            option_menu = tk.OptionMenu(window,selected_choice,*conditionals)
            option_menu.grid(row=i, column=1, padx=10, pady=5)
            menus.append(option_menu)
            
            entry = tk.Entry(window,width=50,validate="key",validatecommand=vcmd)
            entry.grid(row=i, column=2,padx=10, pady=5)
            entries.append(entry)
            choices.append(["int",selected_choice,i,entry])
            
        elif columns[2] == "float":
            selected_choice = tk.StringVar(window)
            selected_choice.set(conditionals[0])
            
            option_menu = tk.OptionMenu(window,selected_choice,*conditionals)
            option_menu.grid(row=i, column=1, padx=10, pady=5)
            menus.append(option_menu)
            
            entry = tk.Entry(window,width=50,validate="key",validatecommand=vcmd2)
            entry.grid(row=i, column=2,padx=10, pady=5)
            entries.append(entry)
            choices.append(["float",selected_choice,i,entry])
        
        elif columns[2] == "bool":
            selected_choice = tk.StringVar(window)
            selected_choice.set(booleans[0])
             
            option_menu = tk.OptionMenu(window,selected_choice,*booleans)
            option_menu.grid(row=i, column=1, padx=10, pady=5)
            menus.append(option_menu)
            
            choices.append(["bool",selected_choice,i])
        elif columns[2] == "string":
            selected_choice = tk.StringVar(window)
            selected_choice.set(string_options[0])
            
            option_menu = tk.OptionMenu(window,selected_choice,*string_options)
            option_menu.grid(row=i, column=1, padx=10, pady=5)
            menus.append(option_menu)
            
            entry = tk.Entry(window,width=50,validate="key")
            entry.grid(row=i, column=2,padx=10, pady=5)
            entries.append(entry)
            choices.append(["string",selected_choice,i,entry])
        elif columns[2] == "time":
            label = tk.Label(window, text = "Between")
            label.grid(row=i, column=1, padx=10, pady=5)
            labels.append(label)
            
            label2 = tk.Label(window, text = "mm/dd/yyyy")
            label2.grid(row=i, column=2, padx=10, pady=5)
            labels.append(label2)
            
            entry = tk.Entry(window,width=50,validate="key")
            entry.grid(row=i, column=3,padx=10, pady=5)
            entries.append(entry)
            
            label3 = tk.Label(window, text = "AND")
            label3.grid(row=i, column=4, padx=10, pady=5)
            labels.append(label3)
            
            entry2 = tk.Entry(window,width=50,validate="key")
            entry2.grid(row=i, column=5,padx=10, pady=5)
            entries.append(entry2)
            choices.append(["time",i,entry,entry2])
             
    finalize_button = tk.Button(window, text="Finalize choices", command= lambda : get_selected_choice2(choices, selected_condtionals))
    finalize_button.grid(row=len(selected_columns), column=0, pady=10)
    
    close_button = ttk.Button(window, text="Next", command=window.destroy)
    close_button.grid(row=len(selected_columns)+1, column=0, pady=10)
    
    window.update_idletasks()
    current_height = window.winfo_height()
    window.geometry(f"1500x{current_height}")
    window.mainloop()
    return selected_condtionals        
            

            
            
    
    
"""" 
    int64/32/16/8
    uint64/32/16/8
    float64/32/16
    bool
    object(this includes strings)
    datetime64
    Timedelta
"""
    
    



selected_columns = []
finalize_selections = []
og_selected = []
test = []
df = read_dataframe(test_path)
column_names = df.columns.to_list()
#test_data_type = gather_data_types(df,column_names)
#print(test_data_type)
column_selection(column_names,column_names,selected_columns,og_selected)
print(WHERE_statement(df,selected_columns,og_selected))
# print(selected_columns)
# print(og_selected)
# finalize_selections = ascending_or_descending(selected_columns)
# print(selected_columns)
# print(finalize_selections)
# print(ORDER_BY_statement(selected_columns,finalize_selections))
#print(LIMIT_statement())

