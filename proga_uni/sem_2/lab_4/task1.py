from tkinter import *
from tkinter import ttk

def show_information():
    information = ["Author - Agonek", "Language - Python", "Day of release - 17/04/24"]
    information_var = StringVar(value=information)
    information_listbox = Listbox(listvariable=information_var)
    information_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

def isNegative(number):
    if int(number) < 0:
        errmsg.set("Your number should be positive")
        return False
    else:
        errmsg.set("")
        return True
def finish():
    tk.destroy()
    print("App is closing...")

def clearing():
    entry1.delete(0, END)
    entry2.delete(0, END)

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = selected_operation.get()
        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            if num2 == 0:
                result.set("Div by zero")
            else:
                result.set(round(num1 / num2, 2))
    except ValueError:
        result.set("Invalid input")

if __name__ == "__main__":
    tk = Tk()
    tk.option_add("*tearOff", FALSE)
    tk.title('Graphic calculator')
    tk.geometry('450x650+320+240')

    position = {"padx": 6, "pady": 6, "anchor": NW}
    activities = ["Calculator", "Rectangle"]
    selected_activity = StringVar(value=activities[0])

    header = ttk.Label(text="Choose activity")
    header.pack(**position)

    def select():
        header.config(text=f"{selected_activity.get()} is choosed")

    for activity in activities:
        act_btn = ttk.Radiobutton(text=activity, value=activity, variable=selected_activity, command=select)
        act_btn.pack(**position)

    errmsg = StringVar()


    entry1 = ttk.Entry(width=10, validate="key", validatecommand=(tk.register(isNegative), "%P"))
    entry2 = ttk.Entry(width=10, validate="key", validatecommand=(tk.register(isNegative), "%P"))
    entry1.place(x=8, y=120)
    entry2.place(x=110, y=120)
    calculate_button = ttk.Button(text="Calc", command=calculate, width=4)
    calculate_button.place(x=219, y=120)

    result = StringVar()
    result_label = ttk.Label(textvariable=result, width=12)
    result_label.place(x=330, y=120)

    selected_operation = StringVar(value="+")
    operation_menu = ttk.OptionMenu(tk, selected_operation, "+", "+", "-", "*", "/")
    operation_menu.place(x=280, y=120)

    error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
    error_label.place(x=8, y=150)

    menu = Menu(tk)
    tk.config(menu=menu)

    file_menu = Menu(menu)
    file_menu.add_command(label="Exit", command=finish)

    operation_menu = Menu(menu)
    operation_menu.add_command(label="+")
    operation_menu.add_command(label="-")
    operation_menu.add_command(label="*")
    operation_menu.add_command(label="/")

    operations_menu = Menu(menu)
    operations_menu.add_command(label="Clear data", command=clearing)
    operations_menu.add_separator()
    operations_menu.add_cascade(label="Choosing operation", menu=operation_menu)

    menu.add_cascade(label="File", menu=file_menu)
    menu.add_cascade(label="Operations", menu=operations_menu)
    menu.add_command(label="Info", command=show_information)

    tk.resizable(True, True)
    tk.minsize(380, 550)
    tk.maxsize(1200, 700)
    tk.iconbitmap(default="icon.ico")
    tk.attributes("-alpha", 0.85)
    tk.mainloop()
