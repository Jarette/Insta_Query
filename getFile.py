import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

"""
Name: error_message 

Description: 
    TThis function will display an error message with the title and the message
    passed in
"""
def error_message(message:str, title:str):
    
    # Create a hidden Tkinter root window
    root = tk.Tk()
    
    # Hide the main window
    root.withdraw()
    
    # displaying the error message
    messagebox.showerror(message,title)
    
    # Destroy the hidden root window closing the error message window
    root.destroy()

"""
Name: select_file 

Description: 
    This function opens a file selection window and a file from user files 
    and save the file path.
"""
def select_file():
    # Create a hidden Tkinter root window
    root = tk.Tk()
    
    # Hide the main window
    root.withdraw()
    
    # Open the file selection dialog/window
    path = filedialog.askopenfilename(
        # name of the window
        title = "Select A File",
        # allowing the user to sort the files looking for a csv or xlsx file
        filetypes=(("Excel files","*.xlsx"), ("CSV files","*.csv"),("All files","*.*"))
        )
    
    # Destroy the hidden root window after selection
    root.destroy()
    
    # returning the final path
    return path

"""
Name: get_file_extension 

Description: 
    getting the file extension from file path passed in 
"""
def get_file_extension(path:str):
    
    # spliting the path in to directory and file name 
    _,file_name = os.path.split(path)
    
    # spliting the file name into name and extension 
    _,ext = os.path.splitext(file_name)
    
    # returing the file extension
    return ext


"""
Name: validating_file

Description: 
    asks the user for a file and ensure that it is either in a csv or a xlsx format
    by checking the extension and if its not one of the valid formats makes a pop up
    message and ask the user to enter a new file until valid file is selected 
"""
def validating_file():
    # get inital file from user 
    selected_file = select_file()
    
    # flag checking if valid file was selected 
    invalid = True
    while invalid:
        
        # no file selected 
        if not selected_file:
            
            # display error message
            error_message("Invalid File", "Please enter a file of the following formats .csv or .xlsx")
            # asking user for new file 
            selected_file = select_file()
            # move on to next iteration of loop    
            continue
        else:
            # if file entered get extension 
            ext = get_file_extension(selected_file)
            
            # checking if file is not csv and a xlsx 
            if ext != ".csv" and ext !=".xlsx":
                error_message("Invalid File", "Please enter a file of the following formats .csv or .xlsx")
                selected_file = select_file()   
                continue
            else:
                # valid file extension found 
                invalid = False
    # retur the final path
    return selected_file
                
print(validating_file())