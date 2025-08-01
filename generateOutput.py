import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from theDataframe import read_dataframe

test_path = "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx"

# path at home "C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

# path for at work "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx"


def output_window(title:str,table:pd.DataFrame,orginal_column_names:list):
    window = tk.Tk()
    window.title(title)
    
    frame = ttk.Frame(window)
    frame.pack(fill="both",expand=True)
    
    tree = ttk.Treeview(window, columns=orginal_column_names, show="headings")
    
    for col in orginal_column_names:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    
    for _,row in df.iterrows():
        tree.insert("","end",values=list(row))
    
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side='right', fill = 'y')

    save_button = ttk.Button(window, text="Save",command= save_dataframe(df,"out.xlsx"))
    save_button.pack(pady= 20)

    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)
    
    tree.pack(fill="both",expand = True)
    window.mainloop()


def save_dataframe(df:pd.DataFrame, file_name:str):
    root = tk.Tk()
    
    # Hide the main window
    root.withdraw()
    
    # Open the file selection dialog/window
    path = filedialog.asksaveasfilename(
        # name of the window
        title = "Save the file",
        # allowing the user to sort the files looking for a csv or xlsx file
        filetypes=(("Excel files","*.xlsx"), ("CSV files","*.csv"),("All files","*.*"))
        )
    
    # Destroy the hidden root window after selection
    root.destroy()

    _,file_name = os.path.split(path) 
    writer = pd.ExcelWriter(path,engine="xlsxwriter")
    df.to_excel(writer, index = False, header = True)

df = read_dataframe(test_path)
columns = df.columns.to_list()
output_window("Final Query Results",df,columns)
#save_dataframe(df,"out.xlsx")


