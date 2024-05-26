from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning


# Вспомогательные функции
def show_information():
    information = ["Author - Agonek", "Language - Python", "Day of release - 27/04/24"]
    str_info = "\n".join(information)
    showinfo(title="Information", message=str_info)

def finish():
    tk.destroy()
    print("App is closing...")

# Классы для кнопок пиццы и размера
class PizzaButton(ttk.Radiobutton):
    def __init__(self, master, text, row, column, columnspan=1):
        self.variable = BooleanVar()
        super().__init__(master, text=text, value=True, variable=self.variable, command=self.temporary_decision)
        self.grid(row=row, column=column, columnspan=columnspan)

    def temporary_decision(self):
        pass

class SizeButton(ttk.Radiobutton):
    def __init__(self, master, text, row, column, columnspan=1):
        self.variable = BooleanVar()
        super().__init__(master, text=text, value=True, variable=self.variable, command=self.temporary_decision)
        self.grid(row=row, column=column, columnspan=columnspan)

    def temporary_decision(self):
        pass

# Основной класс приложения
class PizzaApp:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.root.option_add("*tearOff", FALSE)
        self.root.title('Agonek\'s Pizza')
        self.root.geometry('357x650+320+240')

        ttk.Label(text="Name:").grid(row=0, column=0)
        ttk.Entry(width=15).grid(row=0, column=1)

        PizzaButton(self.root, "Pepperoni", row=1, column=0)
        PizzaButton(self.root, "Barbeque", row=1, column=1)
        PizzaButton(self.root, "PizzaSeafood", row=1, column=2)

        SizeButton(self.root, text="30cm", row=2, column=0)
        SizeButton(self.root, text="35cm", row=2, column=1)
        SizeButton(self.root, text="40cm", row=2, column=2)

        ttk.Button(text="Change Ingredients").grid(row=3, column=1)
        ttk.Button(text="Add one more pizza").grid(row=4, column=1)
        ttk.Button(text="Order").grid(row=5, column=1)

        self.create_menu()

        self.root.resizable(True, True)
        self.root.minsize(357, 550)
        self.root.maxsize(1200, 700)
        self.root.iconbitmap(default="icon.ico")

    def create_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="Exit", command=finish)

        operation_menu = Menu(menu)
        operation_menu.add_command(label="waiting list", command=self.temporary_decision)
        operation_menu.add_command(label="new order", command=self.temporary_decision)

        operations_menu = Menu(menu)
        operations_menu.add_command(label="Clear data", command=self.clearing)
        operations_menu.add_separator()
        operations_menu.add_cascade(label="Choosing operation", menu=operation_menu)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Operations", menu=operations_menu)
        menu.add_command(label="Info", command=show_information)

    def temporary_decision(self):
        pass

    def clearing(self):
        pass

# Запуск приложения
if __name__ == "__main__":
    tk = Tk()
    app = PizzaApp(tk)
    tk.mainloop()
