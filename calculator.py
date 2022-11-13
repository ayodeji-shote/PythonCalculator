# Imports used for the python module 
from tkinter import ttk, Entry,Button, StringVar,Tk

class Calculator:
    # "__init__" is a reseved method in python classes. 
    # It is known as a constructor in object oriented concepts. 
    # This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
    # in this case init is used to initialize the calculator object with the title of master
    def __init__(self,master): 
        # Title is the name of the calculator object
        # geometry is the width and height of the calculator object
        # Config bg is the background colour of the object
        # resizable is choice to be able to change the size of the x and the y properties of the calculator object
        master.title("calculator ")
        master.geometry("400x500+0+0")
        master.config(bg="grey")
        master.resizable(False,False)
        
        # The equation field is the part of the calculator that shows what the user is typing 
        # The entry_value is what the user enters in the calculator field 
        self.equation = StringVar()
        self.entry_value = ""
        #Entry is the details of the area that the numbers and equations will go width is the width of the area,
        # bg is the background colour 
        # font is the font and the number next to it is the size of the font
        # textvariable is the text which is going to be handled by the equation called string var 
        # place is the position of the text
        Entry(width=20,bg="#C5D6D8",font=("Arial Bold",80),textvariable = self.equation).place(x=5,y=0)
        
        # The buttons are to generate the function buttons buttons for the calculator
        Button(width=13,height = 4,text="(",relief= "flat",bg="white",command=lambda:self.show("(")).place(x=5,y=130)
        Button(width=12,height = 4,text=")",relief= "flat",bg="white",command=lambda:self.show(")")).place(x=108,y=130)
        Button(width=12,height = 4,text="%",relief= "flat",bg="white",command=lambda:self.show("%")).place(x=205,y=130)
        Button(width=12,height = 4,text="/",relief= "flat",bg="white",command=lambda:self.show("/")).place(x=301,y=130)
        
        # The buttons are to generate the function buttons buttons for the calculator
        Button(width=13,height = 4,text="1",relief= "flat",bg="white",command=lambda:self.show(1)).place(x=5,y=205)
        Button(width=12,height = 4,text="2",relief= "flat",bg="white",command=lambda:self.show(2)).place(x=108,y=205)
        Button(width=12,height = 4,text="3",relief= "flat",bg="white",command=lambda:self.show(3)).place(x=205,y=205)
        Button(width=12,height = 4,text="x",relief= "flat",bg="white",command=lambda:self.show("*")).place(x=301,y=205)
            
        # The buttons are to generate the function buttons buttons for the calculator
        Button(width=13,height = 4,text="4",relief= "flat",bg="white",command=lambda:self.show(4)).place(x=5,y=280)
        Button(width=12,height = 4,text="5",relief= "flat",bg="white",command=lambda:self.show(5)).place(x=108,y=280)
        Button(width=12,height = 4,text="6",relief= "flat",bg="white",command=lambda:self.show(6)).place(x=205,y=280)
        Button(width=12,height = 4,text="-",relief= "flat",bg="white",command=lambda:self.show("-")).place(x=301,y=280)
        
        # The buttons are to generate the function buttons buttons for the calculator
        Button(width=13,height = 4,text="7",relief= "flat",bg="white",command=lambda:self.show(7)).place(x=5,y=355)
        Button(width=12,height = 4,text="8",relief= "flat",bg="white",command=lambda:self.show(8)).place(x=108,y=355)
        Button(width=12,height = 4,text="9",relief= "flat",bg="white",command=lambda:self.show(9)).place(x=205,y=355)
        Button(width=12,height = 4,text="+",relief= "flat",bg="white",command=lambda:self.show("+")).place(x=301,y=355)

        # The buttons are to generate the function buttons buttons for the calculator
        Button(width=13,height = 4,text="c",relief= "flat",bg="white",command=self.clear).place(x=5,y=430)
        Button(width=12,height = 4,text="0",relief= "flat",bg="white",command=lambda:self.show(0)).place(x=108,y=430)
        Button(width=12,height = 4,text=".",relief= "flat",bg="white",command=lambda:self.show(".")).place(x=205,y=430)
        Button(width=12,height = 4,text="=",relief= "flat",bg="white",command=self.solve).place(x=301,y=430)

    # This method handles actually appending and showing the value on the calculator screen entry.
    # entry_value is what is displayed on the calculator screen and the += is used to add what ever value you enter to put in 
    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
    def clear(self):
        self.entry_value=""
        self.equation.set(self.entry_value)
    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)
root = Tk()
calculator = Calculator(root)
root.mainloop()