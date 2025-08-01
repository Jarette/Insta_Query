import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from theDataframe import read_dataframe
from getFile import get_file_extension

test_path = "C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

# "C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

# path for at work "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx"

"""
Name: output_window
Description: This function displays the data frame generated from the query and gives 
Then gives you the option to save the data frame as either an excel file or a 
csv file. 
"""
def output_window(title:str,table:pd.DataFrame,orginal_column_names:list):
    
    # creating the window
    window = tk.Tk()
    #giving the window a title
    window.title(title)
    
    # creating the frame to display the data
    frame = ttk.Frame(window)
    frame.pack(fill="both",expand=True)
    
    # tree that will display the table
    tree = ttk.Treeview(frame, columns=orginal_column_names, show="headings")
    
    #placing the columns on the tree
    for col in orginal_column_names:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    
    # placing the rows in the tree 
    for _,row in table.iterrows():
        tree.insert("","end",values=list(row))
    
    # adding a horizontal scroll bar
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side='right', fill = 'y')
    tree.pack(fill="both",expand = True)

    # making a frame for the buttons
    button_frame = ttk.Frame(window)
    button_frame.pack(pady=10)
    
    # button to save the data frame
    save_button = ttk.Button(button_frame, text="Save",command=lambda: save_dataframe(table))
    save_button.pack(pady= 20)
    
    # button to close the window 
    close_button = ttk.Button(button_frame, text="Close", command=window.destroy)
    close_button.pack(pady=10)
    
    window.mainloop()

"""
Name: save_dataframe
Description: function to save the data frame to a file with a save as window 
and allows the user to save as either a CSV or a XLSX file
"""
def save_dataframe(df:pd.DataFrame):
    root = tk.Tk()
    
    # Hide the main window
    root.withdraw()
    
    # Open the file selection dialog/window
    path = filedialog.asksaveasfilename(
        defaultextension= ".xlsx",
        # name of the window
        title = "Save the file",
        # allowing the user to sort the files looking for a csv or xlsx file
        filetypes=(("Excel files","*.xlsx"), ("CSV files","*.csv"))
        )
    
    # Destroy the hidden root window after selection
    root.destroy()
    
    # getting the extension of where the file will be stored 
    ext = get_file_extension(path)
    
    # picking the correct save function based on the extension
    if ext == ".xlsx":
        df.to_excel(path, index = False, header = True)
    else:
        df.to_csv(path,index=False)

#df = read_dataframe(test_path)
#columns = df.columns.to_list()
#output_window("Final Query Results",df,columns)


