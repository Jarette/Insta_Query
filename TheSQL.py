import pandas as pd
import pandasql as pdsql
from theDataframe import column_data_type
from theDataframe import read_dataframe
import tkinter as tk
from tkinter import ttk

test_path = "C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

#"C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

# path for at work "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx"

# help desk path : "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx" 

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

"""
Name: gather_data_types
Description: Gathers the data type of the columns entered into the function 
assigning a tag to that will be used for later processing of column values 
"""
def gather_data_types(df:pd.DataFrame, selected_columns:list):
    data_types = []
    # traversing list of columns 
    for col in selected_columns:
        # collecting the data types
        data_types.append(column_data_type(df,col))
    # return list of data types
    return data_types

"""
Name: get_selected_columns2
Description: Similar to the get_selected_columns function but customized specifically for use 
to gather data for the WHERE statement 
"""
def get_selected_choice2(choices:list[tk.StringVar,int],final_choices:list):
    #gathering all the choices from the Where statement window
    for choice in choices:
        # if the number of data gathered is 4 meaning that this is from a int, float, string, or time column data
        if len(choice) == 4:
            # if that data type is time 
            if choice[0] == "time":
                # collecting the data type, index, starting date and ending date
                final_choices.append([choice[0],choice[1],choice[2].get(),choice[3].get()])
            else:
                #else collecting the data type, index, and box selection and user entered data 
                final_choices.append([choice[0],choice[2],choice[1].get(),choice[3].get()])
        
        # if the choice contains 3 items this means it is a bool column 
        elif len(choice) == 3:
            # collecting the data type, index, and true or false value 
            final_choices.append([choice[0],choice[2],choice[1].get()])
            
        # if the choice contains 2 items this is a conditional used if there are multiple selected columns 
        elif len(choice) == 2:
            # collecting a conditional tag, and collecting the conditional 
            final_choices.append([choice[0],choice[1].get()])  

"""
Name: only_allow_numbers
Description: validation functions used to ensure that data entered is a number (integer and float)
"""
def only_allow_numbers(new_value):
    if new_value == "":
        return True
    try:
        float(new_value)
        return True
    except ValueError:
        return False

"""
Name: WHERE_statement
Description: This function will display windows that will allow the user to enter data that will be used to generate 
the SQL WHERE Statement. 
"""    
def WHERE_statement(df:pd.DataFrame, selected_columns:list, og_column_names:list):
    # collecting the datatypes of the different columns 
    data_types = gather_data_types(df,selected_columns)
    
    # joining lists consisting of the names (original and formated) and datatype of each columns 
    og_selected_datatypes = zip(og_column_names,selected_columns,data_types)
    
    # list containing the various options 
    conditionals = ["equal","not equal","less than", "less than or eqaul to", "greater than", "greater than or equal to"]
    booleans = ["True", "False"]
    string_options = ["Starts with", "Contains", "Ends with","Does not starts with", "Does not Contains", "Does not Ends with"]
    AND_OR_choices = ["AND","OR"]
    
    # list containing the different elements for the windows 
    labels = []
    choices = []
    menus = []
    entries = []
    selected_condtionals = []
    
    # creating the TK windows
    window = tk.Tk()
    window.title("WHERE Input")
    
    # validation functions used to ensure data being eneterd is a integer or  float respectively
    vcmd = (window.register(only_allow_integers), "%P")
    vcmd2 = (window.register(only_allow_numbers), "%P")
    
    # generating the window based on the selected graphs 
    for i,columns in enumerate(og_selected_datatypes):
        
        # placing the name of the column on the window
        label = tk.Label(window, text = columns[0])
        label.grid(row=i, column=0, padx=10, pady=5)
        labels.append(label)
        
        # if the data type of the column being processed is a integer 
        if columns[2] == "int":
            
            # creating drop down window for user to pick bolean conditions (<,>,=,>=,<=) etc
            selected_choice = tk.StringVar(window)
            selected_choice.set(conditionals[0])
            
            option_menu = tk.OptionMenu(window,selected_choice,*conditionals)
            option_menu.grid(row=i, column=1, padx=10, pady=5)
            menus.append(option_menu)
            
            # box allowing the user to type an integer (does check to make sure it is integer)
            entry = tk.Entry(window,width=50,validate="key",validatecommand=vcmd)
            entry.grid(row=i, column=2,padx=10, pady=5)
            entries.append(entry)
            choices.append(["int",selected_choice,i,entry])

            # generate this window if there are multiple columns or this isnt the last columns to be generated 
            if len(selected_columns) > 1 and i < len(selected_columns) - 1:
                
                # generate a drop down window asking for AND or OR that is used only when multiple columns are selected 
                selected_choice2 = tk.StringVar(window)
                selected_choice2.set(AND_OR_choices[0])
            
                option_menu = tk.OptionMenu(window,selected_choice2,*AND_OR_choices)
                option_menu.grid(row=i, column=3, padx=10, pady=5)
                menus.append(option_menu)
                choices.append(["conditions", selected_choice2])

        # similar to the integer data type but for floats
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

            if len(selected_columns) > 1 and i < len(selected_columns) - 1:
                selected_choice2 = tk.StringVar(window)
                selected_choice2.set(AND_OR_choices[0])
            
                option_menu = tk.OptionMenu(window,selected_choice2,*AND_OR_choices)
                option_menu.grid(row=i, column=3, padx=10, pady=5)
                menus.append(option_menu)
                choices.append(["conditions", selected_choice2])
        
        # if checking if the data type is a boolean 
        elif columns[2] == "bool":
            
            # generate drop down asking the user to pick true or false 
            selected_choice = tk.StringVar(window)
            selected_choice.set(booleans[0])
             
            option_menu = tk.OptionMenu(window,selected_choice,*booleans)
            option_menu.grid(row=i, column=1, padx=10, pady=5)
            menus.append(option_menu)
            choices.append(["bool",selected_choice,i])

            if len(selected_columns) > 1 and i < len(selected_columns) - 1:
                selected_choice2 = tk.StringVar(window)
                selected_choice2.set(AND_OR_choices[0])
            
                option_menu = tk.OptionMenu(window,selected_choice2,*AND_OR_choices)
                option_menu.grid(row=i, column=3, padx=10, pady=5)
                menus.append(option_menu)
                choices.append(["conditions", selected_choice2])
                
         # if checking if the data type is a string
        elif columns[2] == "string":
            
            # generate a drop down window which allows the user to state if thier looking for a string to contain, start, end or doesnt not have the string entered int he box 
            selected_choice = tk.StringVar(window)
            selected_choice.set(string_options[0])
            
            option_menu = tk.OptionMenu(window,selected_choice,*string_options)
            option_menu.grid(row=i, column=1, padx=10, pady=5)
            menus.append(option_menu)
            
            # box allowing user ot enter a string
            entry = tk.Entry(window,width=50,validate="key")
            entry.grid(row=i, column=2,padx=10, pady=5)
            entries.append(entry)
            choices.append(["string",selected_choice,i,entry])

            if len(selected_columns) > 1 and i < len(selected_columns) - 1:
                selected_choice2 = tk.StringVar(window)
                selected_choice2.set(AND_OR_choices[0])
            
                option_menu = tk.OptionMenu(window,selected_choice2,*AND_OR_choices)
                option_menu.grid(row=i, column=3, padx=10, pady=5)
                menus.append(option_menu)
                choices.append(["conditions", selected_choice2])

        # if the column is a date/time datatype
        elif columns[2] == "time":
            
            label = tk.Label(window, text = "Between")
            label.grid(row=i, column=1, padx=10, pady=5)
            labels.append(label)
            
            # label showing the format of the date being entered 
            label2 = tk.Label(window, text = "mm/dd/yyyy")
            label2.grid(row=i, column=2, padx=10, pady=5)
            labels.append(label2)
            
            # box allowing the user to enter the date 
            entry = tk.Entry(window,width=50,validate="key")
            entry.grid(row=i, column=3,padx=10, pady=5)
            entries.append(entry)
            
            
            label3 = tk.Label(window, text = "AND")
            label3.grid(row=i, column=4, padx=10, pady=5)
            labels.append(label3)
            # enter the second date 
            entry2 = tk.Entry(window,width=50,validate="key")
            entry2.grid(row=i, column=5,padx=10, pady=5)
            entries.append(entry2)
            choices.append(["time",i,entry,entry2])

            if len(selected_columns) > 1 and i < len(selected_columns) - 1:
                selected_choice2 = tk.StringVar(window)
                selected_choice2.set(AND_OR_choices[0])
            
                option_menu = tk.OptionMenu(window,selected_choice2,*AND_OR_choices)
                option_menu.grid(row=i, column=6, padx=10, pady=5)
                menus.append(option_menu)
                choices.append(["conditions", selected_choice2])
      
    # This button then collects all the selection from the window        
    finalize_button = tk.Button(window, text="Finalize choices", command= lambda : get_selected_choice2(choices, selected_condtionals))
    finalize_button.grid(row=len(selected_columns), column=0, pady=10)
    
    # closes the windoow
    close_button = ttk.Button(window, text="Next", command=window.destroy)
    close_button.grid(row=len(selected_columns)+1, column=0, pady=10)
    
    # ensures the window is large enough to display data 
    window.update_idletasks()
    current_height = window.winfo_height()
    window.geometry(f"1500x{current_height}")
    window.mainloop()
    
    # returning a list containing all the selections from the users 
    return selected_condtionals        

"""
Name: generate_WHERE_statement
Description: This function takes the list of selections from the Where statement function and generates the appriopriately formated 
sql WHERE statement using this data 
""" 
def generate_WHERE_statement(selected_columns:list, WHERE_info:list):
    # inializing the where statement 
    Where_statement = "WHERE "
    
    # traversing the list of user selections 
    for info in WHERE_info:
        # if the data relates to a integer or float column 
        if info[0] == "int" or info[0] == "float":
            # get the column name 
            Where_statement = Where_statement + f"{selected_columns[info[1]]} "
            
            # baased on the condtional selected generate the approriate symbol
            if info[2] == "equal":
                Where_statement = Where_statement + f"= {info[3]} "
            elif info[2] == "not equal":
                Where_statement = Where_statement + f"!= {info[3]} "
            elif info[2] == "less than":
                Where_statement = Where_statement + f"< {info[3]} "
            elif info[2] == "less than or equal to":
                Where_statement = Where_statement + f"<= {info[3]} "
            elif info[2] == "greater than":
                Where_statement = Where_statement + f"> {info[3]} "
            elif info[2] == "greater than or equal to":
                Where_statement = Where_statement + f">= {info[3]} "
                
        # this is for the between conditionals if there are multiple selected columns 
        elif info[0] == "conditions":
            Where_statement = Where_statement + f"{info[1]} "
        
        # genrate the statemente checking for bolean columsn 
        elif info[0] == "bool":
            Where_statement = Where_statement + f"{selected_columns[info[1]]} IS {info[2]} "
            
        # if the data in the columns is a string 
        elif info[0] == "string":
            
            # adding selected columns
            Where_statement = Where_statement + f"{selected_columns[info[1]]} "
            
            # baased on the condtional selected generate the approriate wildcard
            if info[2] == "Starts with":
                Where_statement = Where_statement + f"LIKE \"{info[3]}%\" "
            elif info[2] == "Contains":
                Where_statement = Where_statement + f"LIKE \"%{info[3]}%\" "
            elif info[2] == "Ends with":
                Where_statement = Where_statement + f"LIKE \"%{info[3]}\" "
            elif info[2] == "Does not starts with":
                Where_statement = Where_statement + f"NOT LIKE \"{info[3]}%\" "
            elif info[2] == "Does not Contains":
                Where_statement = Where_statement + f"NOT LIKE \"%{info[3]}%\" "
            elif info[2] == "Does not Ends with":
                Where_statement = Where_statement + f"NOT LIKE \"%{info[3]}\" "
        elif info[0] == "time":
            Where_statement = Where_statement + f"{selected_columns[info[1]]} BETWEEN #{info[2]}# AND #{info[3]}# "
            
    # return the final where statement       
    return Where_statement       

            
    


# selected_columns = []
# finalize_selections = []
# og_selected = []
# test = []
# df = read_dataframe(test_path)
# column_names = df.columns.to_list()
# #test_data_type = gather_data_types(df,column_names)
# #print(test_data_type)
# column_selection(column_names,column_names,selected_columns,og_selected)
# where_info = WHERE_statement(df,selected_columns,og_selected)
# print(generate_WHERE_statement(selected_columns,where_info))
# # print(selected_columns)
# # print(og_selected)
# # finalize_selections = ascending_or_descending(selected_columns)
# # print(selected_columns)
# # print(finalize_selections)
# # print(ORDER_BY_statement(selected_columns,finalize_selections))
# #print(LIMIT_statement())

