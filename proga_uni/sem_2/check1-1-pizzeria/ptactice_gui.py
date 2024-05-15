from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning

def change_places():
    pass
def temprary_desicion():
    pass

def show_information():
    information = ["Author - Agonek", "Language - Python", "Day of release - 27/04/24"]
    str_info = "\n".join(information)
    showinfo(title="Information", message=str_info)

def finish():
    tk.destroy()
    print("App is closing...")

def clearing():
    pass

tk = Tk()
tk.option_add("*tearOff", FALSE)
tk.title('Agonek\'s Pizza')
tk.geometry('357x650+320+240')

name_label = ttk.Label(text="Name:").grid(row=0, column=0)
name_entry = ttk.Entry(width=15).grid(row=0, column=1)


class PizzaButton(ttk.Radiobutton):
    def __init__(self, master, text, row, column, columnspan):
        self.variable = BooleanVar()
        super().__init__(master, text=text, value=True, variable=self.variable, command=self.temporary_decision)
        self.grid(row=row, column=column, columnspan=columnspan)

    def temporary_decision(self):
        pass

class SizeButton(ttk.Radiobutton):
    def __init__(self, master, text, row, column, columnspan):
        self.variable = BooleanVar()
        super().__init__(master, text=text, value=True, variable=self.variable, command=self.temporary_decision)
        self.grid(row=row, column=column, columnspan=columnspan)

    def temporary_decision(self):
        pass


pepperoni_btn = PizzaButton(tk, "Pepperoni", row=1, column=0, columnspan=1)
barbeque_btn = PizzaButton(tk, "Barbeque", row=1, column=1, columnspan=1)
seafood_btn = PizzaButton(tk, "PizzaSeafood", row=1, column=2, columnspan=1)

small_size_btn = SizeButton(tk, text="30cm", row=2, column=0, columnspan=1)
medium_size_btn = SizeButton(tk,  text="35cm", row=2, column=1, columnspan=1)
big_size_btn = SizeButton(tk,  text="40cm", row=2, column=2, columnspan=1)


change_ingredients_button = ttk.Button(text="Change Ingredients").grid(row=3, column=1)

add_pizza_button = ttk.Button(text="Add one more pizza").grid(row=4, column=1)

order_button = ttk.Button(text="Order").grid(row=5, column=1)

activity_var = IntVar()
activity_var.set(False)

errmsg = StringVar()

'''
change_btn = ttk.Button(text="change args", command=change_places).grid(row=2, column=2)
clear_btn = ttk.Button(text="clear", command=clearing).grid(row=2, column=3)
error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=20)
error_label.grid(row=6, column=0)
'''

menu = Menu(tk)
tk.config(menu=menu)

file_menu = Menu(menu)
file_menu.add_command(label="Exit", command=finish)

operation_menu = Menu(menu)
operation_menu.add_command(label="waiting list", command=temprary_desicion)
operation_menu.add_command(label="new order", command=temprary_desicion)


operations_menu = Menu(menu)
operations_menu.add_command(label="Clear data", command=clearing)
operations_menu.add_separator()
operations_menu.add_cascade(label="Choosing operation", menu=operation_menu)

menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Operations", menu=operations_menu)
menu.add_command(label="Info", command=show_information)

tk.resizable(True, True)
tk.minsize(357, 550)
tk.maxsize(1200, 700)
tk.iconbitmap(default="icon.ico")
tk.mainloop()