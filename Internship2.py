# importing essential libraries
from tkinter import Tk, Button, Label, Entry
import random 
import string
#using ascii characters to build a strong password
def generate_pass(length_of_pass):
    password = ""
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
# concatenating password with random ascii characters  
    for i in range(length_of_pass):
        password += random.choice(characters)
        
    return password

#generating and displaying password
def generate():    
    define_length = int(entry_len.get())                 
    password = generate_pass(define_length)
    pass_label.config(text = "Here is A Password For You:)\n" + password)

#adding GUI to the above code
root = Tk()
root.minsize(300,200)
root.maxsize(450,350)
root.title("Password Generator App")

label_len = Label(root, text="Enter The Length Of Password:")
label_len.pack()

entry_len = Entry(root)
entry_len.pack()

button = Button(root, text = "Generate Password", command = generate) 
button.pack()

pass_label = Label(root, text="Here Is A Password For You:)\n")
pass_label.pack()

root.mainloop()