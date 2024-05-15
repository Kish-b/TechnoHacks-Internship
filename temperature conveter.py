# Importing tkinter module
from tkinter import *  

# Importing random module
import random  


# Creating main window
root = Tk()  
root.title("Temperature Converter")  
root.geometry("400x350") 
root.configure(bg="#17161b")


# Creating a function but you can remove the function if it is not useful
def frame():

    # Creating a function Celsius to Fahrenheit
    def Celsius_to_Fahrenheit():
        ctf.destroy()
        ftc.destroy()

        def convert():
            show.delete(0, END) 
            c = float(data.get()) 
            f = ( c-32)* 5/9
            show.insert(0, f) 

        label = Label(root, text="Enter the Celsius",font=20,bg="#17161b",fg="#fff")  
        label.grid(column=0 , row=1 ,pady=20)  
 
        data = Entry(root, font=("arial", 22))
        data.grid(column=0 , row=2 ,pady=15, padx=35) 
 
        show = Entry(root,width=21 ,font=("arial", 20))
        show.grid(column=0 , row=3 ,pady=15, padx=35) 
                

        convert_button=Button(root, text="Convert",font=("arial",15,"bold"),bd=1,fg="#fff",activebackground="white",bg="#fe9037",command=convert) 
        convert_button.grid(column=0 , row=4 ,pady=15, padx=35 )        

        def back1() :
            back.destroy()
            label.destroy()
            data.destroy()
            show.destroy()
            convert_button.destroy()
            frame()

        back=Button(root, text="Back",font=("arial",15,"bold"),bd=1,fg="#fff",activebackground="white",bg="#fe9037",command=back1) 
        back.grid(column=0 , row=5 ,pady=15, padx=20 )
        

    # Creating a function Fahrenheit to Celsius
    def Fahrenheit_to_Celsius():
        ctf.destroy()
        ftc.destroy()

        def convert():
            show.delete(0, END) 
            f = float(data.get()) 
            c = ( f*1.8)+ 32
            show.insert(0, c) 

        label = Label(root, text="Enter the Fahrenheit",font=20,bg="#17161b",fg="#fff")  
        label.grid(column=0 , row=1 ,pady=20)  
 
        data = Entry(root, font=("arial", 22))
        data.grid(column=0 , row=2 ,pady=15, padx=35) 
 
        show = Entry(root,width=21 ,font=("arial", 20))
        show.grid(column=0 , row=3 ,pady=15, padx=35) 
                

        convert_button=Button(root, text="Convert",font=("arial",15,"bold"),bd=1,fg="#fff",activebackground="white",bg="#fe9037",command=convert) 
        convert_button.grid(column=0 , row=4 ,pady=15, padx=35 )        

        def back1() :
            back.destroy()
            label.destroy()
            data.destroy()
            show.destroy()
            convert_button.destroy()
            frame()

        back=Button(root, text="Back",font=("arial",15,"bold"),bd=1,fg="#fff",activebackground="white",bg="#fe9037",command=back1) 
        back.grid(column=0 , row=5 ,pady=15, padx=20 )


    ctf=Button(root, text="Celsius \n to \n Fahrenheit",font=("arial",15,"bold"),bd=1,fg="#fff",activebackground="white",bg="#fe9037",command=Celsius_to_Fahrenheit) 
    ctf.grid(column=0 , row=0 ,padx=40 ,pady=120 )

    ftc=Button(root, text="Fahrenheit \n to \n Celsius",font=("arial",15,"bold"),bd=1,fg="#fff",activebackground="white",bg="#fe9037",command=Fahrenheit_to_Celsius) 
    ftc.grid(column=1 , row=0,padx=30 ,pady=120)

frame()

root.mainloop()    