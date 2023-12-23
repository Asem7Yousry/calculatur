########## by using tkinter module we build an calculation 
from tkinter import *

#1_bulid the ui that consists of screen , buttons (numbers and operators)
root = Tk()

#size screen
root.minsize(250,390)

#head title 
root.title("calcolatur")

# buld buttons for each number and operation
#label for screen output
screen = Label(root,text="",borderwidth=5,font=3,width=20,height=3,bg="white",fg="black")

# method for each button of number to get different number from each button
def get_button(number):
    # number_but = Label(root,text= number,height=5,width=20,borderwidth=5).grid(row=0,column=1)
    currunt_numbers = screen.cget("text")
    new = currunt_numbers + str(number)
    screen.config(text= new)

# method to remove last digit bit
def remove_last_digit():
    # get data contant
    contant = screen.cget("text")
    # split into digits in list
    contant_digits = list(contant)
    #remove last digit
    contant_digits.pop(-1)
    # return the conatat back to string 
    returned_contant = ''.join(contant_digits)
    screen.config(text=returned_contant)

# to get result and display it
def get_result():
    # to get all data in screen
    currunt_numbers = screen.cget("text")
    # convert it to numirc equation
    result = eval(currunt_numbers)
    #convert result to string
    final_result = str(result)
    #display it screen
    screen.config(text= final_result)

# to clear screen
def cleary():
    screen.config(text="")

# display screen
screen.grid(row=0,column=1)

###creating buttons###
# for numbers 
but1 = Button(root,text="1",command= lambda: get_button(1),width=20,height=2,bg="black", fg="white",font=10).grid(row=1,column=0)
but2 = Button(root,text="2",command= lambda: get_button(2),width=20,height=2,bg="black", fg="white",font=10).grid(row=1,column=1)
but3 = Button(root,text="3",command= lambda: get_button(3),width=20,height=2,bg="black", fg="white",font=10).grid(row=1,column=2)
but4 = Button(root,text="4",command= lambda: get_button(4),width=20,height=2,bg="black", fg="white",font=10).grid(row=2,column=0)
but5 = Button(root,text="5",command= lambda: get_button(5),width=20,height=2,bg="black", fg="white",font=10).grid(row=2,column=1)
but6 = Button(root,text="6",command= lambda: get_button(6),width=20,height=2,bg="black", fg="white",font=10).grid(row=2,column=2)
but7 = Button(root,text="7",command= lambda: get_button(7),width=20,height=2,bg="black", fg="white",font=10).grid(row=3,column=0)
but8 = Button(root,text="8",command= lambda: get_button(8),width=20,height=2,bg="black", fg="white",font=10).grid(row=3,column=1)
but9 = Button(root,text="9",command= lambda: get_button(9),width=20,height=2,bg="black", fg="white",font=10).grid(row=3,column=2)
but0 = Button(root,text="0",command= lambda: get_button(0),width=20,height=2,bg="black", fg="white",font=10).grid(row=4,column=1)

#for operation
but_adding = Button(root,text="+",command= lambda: get_button(" + "),width=20,height=2,bg="black", fg="blue",font=40).grid(row=4,column=0)
but_adding = Button(root,text="_",command= lambda: get_button(" - "),width=20,height=2,bg="black", fg="blue",font=40).grid(row=4,column=2)
but_adding = Button(root,text="X",command= lambda: get_button(" * "),width=20,height=2,bg="black", fg="blue",font=40).grid(row=5,column=0)
but_adding = Button(root,text="%",command= lambda: get_button(" / "),width=20,height=2,bg="black", fg="blue",font=40).grid(row=5,column=1)
but_adding = Button(root,text="=",command= get_result,width=20,height=2,bg="black", fg="blue",font=40).grid(row=5,column=2)

# for (.) for floating numbers 
but_dot = Button(root,text="dot(.)",command= lambda: get_button("."),width=20,height=2,bg="black",fg="red",font=50).grid(row=6,column=0)

# for remove last digit bit
but_remove = Button(root,text="remove digit",command= remove_last_digit,width=20,height=2,bg="black",fg="blue",font=20).grid(row=6,column=1)

# for clear screen
clear_button = Button(root,text="clear",command= cleary,width=20,height=2,bg="black",fg="blue",font=20).grid(row=6,column=2)

#for background color for main window
root.config(bg="gray")

root.mainloop()