import pandas as pd
import pandasql as psql
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from theDataframe import read_dataframe

test_path = "C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

# path at home "C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

# path for at work "C:/Users/jgreene/Desktop/Insta_Query/Insta_Query/Test.xlsx"


def output_window(title:str,table:pd.DataFrame,orginal_column_names:list,formated_column_names:list):
    window = tk.Tk()
    window.title(title)
    
    button_frame = ttk.Frame(window)
    button_frame.pack(side="top", anchor="w", pady=5, padx=5, fill="x")

    save_button = ttk.Button(button_frame, text="Save",command= lambda: save_dataframe(table))
    save_button.pack(side="left", padx=(0, 5))

    close_button = ttk.Button(button_frame, text="Close", command=window.destroy)
    close_button.pack(side = "left")
        
    frame = ttk.Frame(window)
    frame.pack(fill="both",expand=True)
    
    tree = ttk.Treeview(frame, columns=orginal_column_names, show="headings")
    
    for col,name in zip(orginal_column_names,formated_column_names):
        tree.heading(col, text=col)
        max_width = max(table[name].astype(str).map(len).max(), len(name)) * 10
        tree.column(col, anchor='center')
    
    for _,row in table.iterrows():
        tree.insert("","end",values=list(row))
    
    yscrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    xscrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    
    tree.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
    
    tree.pack(side="left", fill="both", expand=True)
    
    yscrollbar.pack(side="right", fill="y")
    xscrollbar.pack(side="bottom", fill="x")

    window.update_idletasks()  
    window.geometry("")
    window.mainloop()


def save_dataframe(df:pd.DataFrame):
    root = tk.Tk()
    
    # Hide the main window
    root.withdraw()
    
    # Open the file selection dialog/window
    path = filedialog.asksaveasfilename(
        # name of the window
        title = "Save the file",
        # allowing the user to sort the files looking for a csv or xlsx file
        filetypes=(("Excel files","*.xlsx"), ("CSV files","*.csv")),
        # Default all saved files as xlsx
        defaultextension= ".xlsx"
        )
    
    # Destroy the hidden root window after selection
    root.destroy()

    # based on the file extension use appriopriate save file function 
    if path:
        if path.endswith(".xlsx"):
            df.to_excel(path,index=False)
        elif path.endswith(".csv"):
            df.to_csv(path,index=False)
    

def perform_query(df:pd.DataFrame, query:str):
    result = psql.sqldf(query,{"df": df})
    return result
        
    
    
# df = read_dataframe(test_path)
# #columns = df.columns.to_list()
# #query = "SELECT Username FROM df"
# #print(perform_query(df,query))
# #output_window("Final Query Results",df,columns)
# save_dataframe(df)


