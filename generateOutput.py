import pandas as pd
import tkinter as tk
from tkinter import ttk
from theDataframe import read_dataframe

test_path = "C:/Users/Jaded/Documents/insta_queary/Insta_Query/Test.xlsx"

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
    
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)
    
    tree.pack(fill="both",expand = True)
    window.mainloop()


df = read_dataframe(test_path)
columns = df.columns.to_list()
output_window("Final Query Results",df,columns)


