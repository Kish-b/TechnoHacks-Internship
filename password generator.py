# Importing tkinter module
from tkinter import *  

# Importing random module
import random  


# Creating main window
root = Tk()  
root.title("Password Generated")  
root.geometry("500x350") 


# Function to generate random password
def rand():
    password.delete(0, END)  # Clearing any existing password
    password_length = int(enter.get()) 
    my_password = ''  

    # Generating random characters and Inserting int0 password 
    for i in range(password_length):
        my_password += chr(random.randint(33, 122))  
    password.insert(0, my_password)  


# Function to copy password to clipboard
def copying():
    root.clipboard_clear()  # Clearing clipboard
    root.clipboard_append(password.get()) 


# Creating label frame
label = LabelFrame(root, text="Enter Number of Characters")  
label.pack(pady=20)  
 
# Creating textbox to enter  
enter = Entry(label, font=("", 24)) 
enter.pack(pady=15, padx=10) 


# Creating textbox for password
password = Entry(root, font=("", 24)) 
password.pack(pady=20) 


# Creating frame for buttons
button_frame = Frame(root)  
button_frame.pack(pady=20)  


# Creating button to generate password
generate = Button(button_frame, text="Generate",font=200, command=rand)  
generate.grid(column=0, row=0, padx=50)  


# Creating button to copy password
copy = Button(button_frame, text="Copy",font=200, command=copying)  
copy.grid(column=1, row=0, padx=50)  


root.mainloop()  
