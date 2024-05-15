from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning

def plus_op():
    oper_one.set(1)
    oper_two.set(2)
    oper_three.set(2)
    oper_four.set(2)
    calculate()
def minus_op():
    oper_two.set(1)
    oper_three.set(2)
    oper_four.set(2)
    oper_one.set(2)
    calculate()

def multi_op():
    oper_three.set(1)
    oper_one.set(2)
    oper_two.set(2)
    oper_four.set(2)
    calculate()

def div_op():
    oper_four.set(1)
    oper_one.set(2)
    oper_three.set(2)
    oper_two.set(2)
    calculate()
def hide_operations():
    plus_btn.grid_remove()
    minus_btn.grid_remove()
    multiplication_btn.grid_remove()
    division_btn.grid_remove()
    result_label.grid_remove()

def change_places():
    value_entry1 = entry1.get()
    value_entry2 = entry2.get()

    # Меняем значения местами
    entry1.delete(0, END)
    entry1.insert(0, value_entry2)

    entry2.delete(0, END)
    entry2.insert(0, value_entry1)

def show_rectangle_buttons():
    hide_operations()
    result_label.grid(row=3, column=1, pady=5, sticky=W)
    square.grid(row=0, column=2, sticky=W, padx=10)
    perimeter.grid(row=0, column=3, sticky=W, padx=10)


def hide_rectangle():
    square.grid_remove()
    perimeter.grid_remove()
    result_label.grid_remove()


def show_operations():
    hide_rectangle()
    result_label.grid(row=3, column=1, pady=5, sticky=W)
    plus_btn.grid(row=0, column=2, sticky=W, padx=10)
    minus_btn.grid(row=0, column=3, sticky=W, padx=10)
    multiplication_btn.grid(row=1, column=2, sticky=W, padx=10)
    division_btn.grid(row=1, column=3, sticky=W, padx=10)


def show_information():
    information = ["Author - Agonek", "Language - Python", "Day of release - 17/04/24"]
    str_info = "\n".join(information)
    showinfo(title="Information", message=str_info)


def open_warning():
    showwarning(title="Предупреждение", message="Your number should be positive")


def finish():
    tk.destroy()
    print("App is closing...")


def clearing():
    entry1.delete(0, END)
    entry2.delete(0, END)
    result_label.grid_remove()


def calculate():
    show_operations()
    if entry1.get() == "" or entry2.get() == "":
        return 0
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ops = ["+", "-", "*", "/"]
        operation = str(oper_one.get()) + str(oper_two.get()) + str(oper_three.get()) + str(oper_four.get())
        print(operation)
        res = []
        for i, op in enumerate(operation):
            if op == "1":
                res.append(ops[i])

        results = []
        for op in res:
            if op == "+":
                results.append(f"{num1} + {num2} = {round(num1 + num2, 2)}")
            elif op == "-":
                results.append(f"{num1} - {num2} = {round(num1 - num2, 2)}")
            elif op == "*":
                results.append(f"{num1} * {num2} = {round(num1 * num2, 2)}")
            elif op == "/":
                if num2 == 0:
                    results.append("Div by zero")
                else:
                    results.append(f"{num1} / {num2} = {round(num1 / num2, 2)}")

        result.set("\n".join(results))
    except ValueError:
        result.set("Invalid input")


def square_perimeter():
    show_rectangle_buttons()
    if entry1.get() == "" or entry2.get() == "":
        return 0
    ops = ["square", "perimeter"]
    res = []
    operation = str(square_var.get()) + str(perimeter_var.get())
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num1 <= 0 or num2 <= 0:
            open_warning()
            return 0
        else:
            for i, v in enumerate(operation):
                if v == "1":
                    res.append(ops[i])
            results = []
            for op in res:
                if op == "square":
                    results.append(f"square = {round(num1 * num2, 2)}")
                elif op == "perimeter":
                    results.append(f"perimeter = {round((num1 + num2) * 2, 2)}")
            result.set("\n".join(results))

            pic = (Canvas(width=200, height=100, bg='white'))
            pic.grid(row=8, column=1, columnspan=2)
            pic.create_rectangle(10, 10, 10*num1, 10*num2)


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

    activity_var = IntVar()
    activity_var.set(False)

    errmsg = StringVar()

    entry1 = ttk.Entry(width=10, validate="key")
    entry2 = ttk.Entry(width=10, validate="key")
    entry1.grid(row=2, column=0, pady=10)
    entry2.grid(row=2, column=1, pady=10)
    '''
    calculate_button = ttk.Button(text="Calculate", command=calculate, width=10)
    calculate_button.grid(row=2, column=3, padx=10, pady=5)
    '''

    oper_one = IntVar()
    oper_one.set(2)
    plus_btn = ttk.Checkbutton(text="+", variable=oper_one, onvalue=1, offvalue=0)
    oper_two = IntVar()
    oper_two.set(2)
    minus_btn = ttk.Checkbutton(text="-", variable=oper_two, onvalue=1, offvalue=0)
    oper_three = IntVar()
    oper_three.set(2)
    multiplication_btn = (ttk.Checkbutton(text="*", variable=oper_three, onvalue=1, offvalue=0))
    oper_four = IntVar()
    oper_four.set(2)
    division_btn = ttk.Checkbutton(text="/", variable=oper_four, onvalue=1, offvalue=0)


    square_var = IntVar()
    square_var.set(2)
    square = ttk.Checkbutton(text="square", variable=square_var, onvalue=1, offvalue=0)
    perimeter_var = IntVar()
    perimeter_var.set(2)
    perimeter = ttk.Checkbutton(text="perimeter", variable=perimeter_var, onvalue=1, offvalue=0)

    calculator_btn = ttk.Radiobutton(text="Calculator", value=False, variable=activity_var, command=calculate).grid(
        row=0, column=0)
    rectangle_btn = ttk.Radiobutton(text="Rectangle", value=True, variable=activity_var, command=square_perimeter).grid(
        row=1, column=0)

    result = StringVar()
    result_label = ttk.Label(textvariable=result, width=15)
    result_label.grid(row=3, column=1, pady=5, sticky=W)

    change_btn = ttk.Button(text="change args", command=change_places).grid(row=2, column=2)
    clear_btn = ttk.Button(text="clear", command=clearing).grid(row=2, column=3)
    error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=20)
    error_label.grid(row=6, column=0)



    menu = Menu(tk)
    tk.config(menu=menu)

    file_menu = Menu(menu)
    file_menu.add_command(label="Exit", command=finish)

    operation_menu = Menu(menu)
    operation_menu.add_command(label="+", command=plus_op)
    operation_menu.add_command(label="-", command=minus_op)
    operation_menu.add_command(label="*", command=multi_op)
    operation_menu.add_command(label="/", command=div_op)

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
    tk.mainloop()
