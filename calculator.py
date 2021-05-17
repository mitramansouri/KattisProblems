from tkinter import *
'''
    This is like the most simple thing man ,i just added somethings together and didnt realy
    care about how it looks , ill come back to it as soon as i got free time.
    '''

root = Tk()
root.title('Mits Calculator')

# Entry
e = Entry(root , width=25,borderwidth=5 , bg='light gray')
e.grid(row=0, column=0, columnspan=3, padx=10 , pady=10)


# show numbers on screen 
def show_numbers(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0 , str(current) + str(number))

# Clear btn
def clear_btn():
    e.delete(0,END )

# Add btn 
def add_btn():
    a = e.get()
    global f_num 
    global math 
    math = 'addition'
    f_num = int(a)
    e.delete(0,END)

# Sub btn
def sub_btn():
    a = e.get()
    global f_num 
    global math 
    math = 'subtraction'
    f_num = int(a)
    e.delete(0,END)

# Mult btn 
def mult_btn():
    a = e.get()
    global f_num 
    global math 
    math = 'multiply'
    f_num = int(a)
    e.delete(0,END)

# Divide btn
def div_btn():
    a = e.get()
    global f_num 
    global math 
    math = 'division'
    f_num = int(a)
    e.delete(0,END)

# Equal btn 
def equal_btn():
    second_num = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0 , f_num+ int(second_num))
    elif math == 'subtraction':
        e.insert(0 , f_num - int(second_num))
    elif math == 'multiply':
        e.insert(0 , f_num * int(second_num))
    elif math == 'division':
        e.insert(0 , f_num / int(second_num))


# Buttons 
btn_0 = Button(root, padx=20, pady=20 , text='0', command=lambda: show_numbers(9))

btn_0.grid(row=4, column=0)

btn_1 = Button(root, padx=20, pady=20 , text='1', command=lambda: show_numbers(1))
btn_2 = Button(root, padx=20, pady=20 , text='2', command=lambda: show_numbers(2))
btn_3 = Button(root, padx=20, pady=20 , text='3', command=lambda: show_numbers(3))

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4 = Button(root, padx=20, pady=20 , text='4', command=lambda: show_numbers(4))
btn_5 = Button(root, padx=20, pady=20 , text='5', command=lambda: show_numbers(5))
btn_6 = Button(root, padx=20, pady=20 , text='6', command=lambda: show_numbers(6))

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7 = Button(root, padx=20, pady=20 , text='7', command=lambda: show_numbers(7))
btn_8 = Button(root, padx=20, pady=20 , text='8', command=lambda: show_numbers(8))
btn_9 = Button(root, padx=20, pady=20 , text='9', command=lambda: show_numbers(9))

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_Clear = Button(root ,padx=19, pady=20, text='C', command=clear_btn)
btn_Clear.grid(row=4, column=1)

btn_eval = Button(root ,padx=20, pady=20, text='=', command=equal_btn)
btn_eval.grid(row=5, column=2)

btn_add = Button(root ,padx=19, pady = 20, text='+', command=add_btn)
btn_sub = Button(root ,padx=21, pady = 20, text='-', command=sub_btn)
btn_mult = Button(root ,padx=20, pady = 20, text='X', command=mult_btn)

btn_add.grid(row=5, column=0)
btn_sub.grid(row=5, column=1)
btn_mult.grid(row=4, column=2)


root.mainloop()