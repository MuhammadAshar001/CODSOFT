#importing essential libraries
import math
from tkinter import Tk,Label,Entry,Button
#creating Calculator class
class Calculator:
    def addition(self, num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1 - num2
    def multiplication(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        if num2 != 0:
            return num1/num2
        else:
            print("Math Error!! :(")
    def remainder(self, num1, num2):
        return num1 % num2
    def power(self, num1, num2):
        return math.pow(num1, num2)
    def square_root(self, num1):
        return math.sqrt(num1)

# Instantiate Calculator class                
calc = Calculator()

def calculate():
    #asking user for inputs
    num1 = float(ent_num1.get())
    num2 = float(ent_num2.get())
    operand = ent_op.get()
    
    
#Calculations based on user input
    if operand == "+":
        result = calc.addition(num1, num2)
    elif operand == "-":
        result = calc.subtraction(num1, num2)
    elif operand == "*":
        result = calc.multiplication(num1, num2)
    elif operand == "/":
        result = calc.division(num1, num2)
    elif operand == "%":
        result = calc.remainder(num1, num2)
    elif operand == "**":
        result = calc.power(num1, num2)
    elif operand == "sqrt":
        result = calc.square_root(num1)
    else:
        print("Invalid Operand!")
   
    result_label.config(text =f"Result: {result}")

# Adding GUI to the above code                
root = Tk()        
root.minsize(300,200)
root.maxsize(600,500)
root.title("Calculator")
label_num1 = Label(root, text="Enter First Number: ")
label_num1.pack()
label_num2 = Label(root, text="Enter Second Number: ")
label_num2.pack()
label_op = Label(root, text= "Select Operand: ")
label_op.pack()
ent_num1 = Entry(root)
ent_num1.pack()
ent_num2 = Entry(root)
ent_num2.pack()
ent_op = Entry(root)
ent_op.pack()
button = Button(root, text= "Calculate", command=calculate)
button.pack()
result_label = Label(root, text="Result: ")
result_label.pack()

root.mainloop()
