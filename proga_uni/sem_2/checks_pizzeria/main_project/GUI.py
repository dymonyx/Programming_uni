'''from tkinter import *
from tkinter import ttk, messagebox
# from order_system import OrderSystem
from pizzas import PizzaPepperoni, PizzaBarbeque, PizzaSeafood
from order import Order

class PizzaButton(ttk.Radiobutton):
    def __init__(self, master, text, command, row, column, columnspan=1):
        self.variable = BooleanVar()
        super().__init__(master, text=text, value=True, variable=self.variable, command=command)
        self.grid(row=row, column=column, columnspan=columnspan)

class SizeButton(ttk.Radiobutton):
    def __init__(self, master, text, command, row, column, columnspan=1):
        self.variable = BooleanVar()
        super().__init__(master, text=text, value=True, variable=self.variable, command=command)
        self.grid(row=row, column=column, columnspan=columnspan)

class PizzaApp:
    def __init__(self, root):
        self.root = root
        self.root.option_add("*tearOff", FALSE)
        self.root.title('Agonek\'s Pizza')
        self.root.geometry('357x650+320+240')
        self.order_manager = OrderManager()
        self.create_widgets()
        self.selected_pizza = None
        self.selected_size = None

    def create_widgets(self):
        ttk.Label(text="Name:").grid(row=0, column=0)
        self.name_entry = ttk.Entry(width=15)
        self.name_entry.grid(row=0, column=1)

        PizzaButton(self.root, "Pepperoni", self.select_pizza_pepperoni, row=1, column=0)
        PizzaButton(self.root, "Barbeque", self.select_pizza_barbeque, row=1, column=1)
        PizzaButton(self.root, "Seafood", self.select_pizza_seafood, row=1, column=2)

        SizeButton(self.root, text="30cm", command=self.select_size_30, row=2, column=0)
        SizeButton(self.root, text="35cm", command=self.select_size_35, row=2, column=1)
        SizeButton(self.root, text="40cm", command=self.select_size_40, row=2, column=2)

        ttk.Button(text="Change Ingredients", command=self.change_ingredients).grid(row=3, column=1)
        ttk.Button(text="Add one more pizza", command=self.add_pizza).grid(row=4, column=1)
        ttk.Button(text="Order", command=self.finalize_order).grid(row=5, column=1)

        self.create_menu()

        self.root.resizable(True, True)
        self.root.minsize(357, 550)
        self.root.maxsize(1200, 700)
        self.root.iconbitmap(default="icon.ico")

    def create_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="Exit", command=self.finish)

        operation_menu = Menu(menu)
        operation_menu.add_command(label="waiting list", command=self.temporary_decision)
        operation_menu.add_command(label="new order", command=self.temporary_decision)

        operations_menu = Menu(menu)
        operations_menu.add_command(label="Clear data", command=self.clearing)
        operations_menu.add_separator()
        operations_menu.add_cascade(label="Choosing operation", menu=operation_menu)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Operations", menu=operations_menu)
        menu.add_command(label="Info", command=self.show_information)

    def select_pizza_pepperoni(self):
        self.selected_pizza = "PizzaPepperoni"

    def select_pizza_barbeque(self):
        self.selected_pizza = "PizzaBarbeque"

    def select_pizza_seafood(self):
        self.selected_pizza = "PizzaSeafood"

    def select_size_30(self):
        self.selected_size = "30cm"

    def select_size_35(self):
        self.selected_size = "35cm"

    def select_size_40(self):
        self.selected_size = "40cm"

    def change_ingredients(self):
        # Placeholder for changing ingredients logic
        pass

    def add_pizza(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        if not self.selected_pizza or not self.selected_size:
            messagebox.showerror("Error", "Please select a pizza and size.")
            return

        self.order_manager.create_order(name)
        size = self.selected_size
        action = self.selected_pizza
        pizza = self.create_pizza(action, size)
        self.modify_ingredients(pizza)
        self.order_manager.add_pizza(pizza)
        messagebox.showinfo("Success", f"Added {action} of size {size}")

    def finalize_order(self):
        if self.order_manager.get_order():
            if messagebox.askyesno("Confirm", "Do you confirm your order?"):
                self.order_manager.finalize_order()
                messagebox.showinfo("Order", "Your order is ready!")
            else:
                messagebox.showinfo("Order", "Order cancelled.")
        else:
            messagebox.showerror("Error", "No pizzas in the order.")

    def show_information(self):
        information = ["Author - Agonek", "Language - Python", "Day of release - 27/04/24"]
        str_info = "\n".join(information)
        messagebox.showinfo("Information", str_info)

    def finish(self):
        self.root.destroy()
        print("App is closing...")

    def temporary_decision(self):
        pass

    def clearing(self):
        pass

    def create_pizza(self, action, size):
        if action == "PizzaPepperoni":
            return PizzaPepperoni(action, size)
        elif action == "PizzaBarbeque":
            return PizzaBarbeque(action, size)
        else:
            return PizzaSeafood(action, size)

    def modify_ingredients(self, pizza):
        # Placeholder for modifying ingredients logic
        pass

# Запуск приложения
if __name__ == "__main__":
    tk = Tk()
    app = PizzaApp(tk)
    tk.mainloop()
'''
from tkinter import *
from tkinter import ttk, messagebox
from pizzas import PizzaPepperoni, PizzaBarbeque, PizzaSeafood
from order import Order

class PizzaButton(ttk.Radiobutton):
    def __init__(self, master, text, command, variable, row, column, columnspan=1):
        super().__init__(master, text=text, value=text, variable=variable, command=command)
        self.grid(row=row, column=column, columnspan=columnspan)

class SizeButton(ttk.Radiobutton):
    def __init__(self, master, text, command, variable, row, column, columnspan=1):
        super().__init__(master, text=text, value=text, variable=variable, command=command)
        self.grid(row=row, column=column, columnspan=columnspan)

class PizzaApp:
    def __init__(self, root, on_order_callback):
        self.root = root
        self.root.option_add("*tearOff", FALSE)
        self.root.title('Agonek\'s Pizza')
        self.root.geometry('357x650+320+240')
        self.on_order_callback = on_order_callback
        self.create_widgets()
        self.order_details = []

    def create_widgets(self):
        ttk.Label(text="Name:").grid(row=0, column=0)
        self.name_entry = ttk.Entry(width=15)
        self.name_entry.grid(row=0, column=1)

        self.pizza_var = StringVar()
        self.size_var = StringVar()

        PizzaButton(self.root, "Pepperoni", self.select_pizza_pepperoni, self.pizza_var, row=1, column=0)
        PizzaButton(self.root, "Barbeque", self.select_pizza_barbeque, self.pizza_var, row=1, column=1)
        PizzaButton(self.root, "Seafood", self.select_pizza_seafood, self.pizza_var, row=1, column=2)

        SizeButton(self.root, text="30cm", command=self.select_size_30, variable=self.size_var, row=2, column=0)
        SizeButton(self.root, text="35cm", command=self.select_size_35, variable=self.size_var, row=2, column=1)
        SizeButton(self.root, text="40cm", command=self.select_size_40, variable=self.size_var, row=2, column=2)

        ttk.Button(text="Change Ingredients", command=self.change_ingredients).grid(row=3, column=1)
        ttk.Button(text="Add one more pizza", command=self.add_pizza).grid(row=4, column=1)
        ttk.Button(text="Order", command=self.finalize_order).grid(row=5, column=1)

        self.create_menu()

        self.root.resizable(True, True)
        self.root.minsize(357, 550)
        self.root.maxsize(1200, 700)
        self.root.iconbitmap(default="icon.ico")

    def create_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="Exit", command=self.finish)

        operation_menu = Menu(menu)
        operation_menu.add_command(label="waiting list", command=self.temporary_decision)
        operation_menu.add_command(label="new order", command=self.temporary_decision)

        operations_menu = Menu(menu)
        operations_menu.add_command(label="Clear data", command=self.clearing)
        operations_menu.add_separator()
        operations_menu.add_cascade(label="Choosing operation", menu=operation_menu)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Operations", menu=operations_menu)
        menu.add_command(label="Info", command=self.show_information)

    def select_pizza_pepperoni(self):
        self.selected_pizza = "PizzaPepperoni"

    def select_pizza_barbeque(self):
        self.selected_pizza = "PizzaBarbeque"

    def select_pizza_seafood(self):
        self.selected_pizza = "PizzaSeafood"

    def select_size_30(self):
        self.selected_size = "30cm"

    def select_size_35(self):
        self.selected_size = "35cm"

    def select_size_40(self):
        self.selected_size = "40cm"

    def change_ingredients(self):
        # Placeholder for changing ingredients logic
        pass

    def add_pizza(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        if not self.pizza_var.get() or not self.size_var.get():
            messagebox.showerror("Error", "Please select a pizza and size.")
            return

        ingredients_to_change = []  # Assuming we gather this information from another part of the GUI
        self.order_details.append({
            'action': self.pizza_var.get(),
            'size': self.size_var.get(),
            'ingredients': ingredients_to_change
        })
        messagebox.showinfo("Success", f"Added {self.pizza_var.get()} of size {self.size_var.get()}")

        # Reset selection
        self.pizza_var.set("")
        self.size_var.set("")

    def finalize_order(self):
        name = self.name_entry.get()
        if not self.order_details:
            messagebox.showerror("Error", "No pizzas in the order.")
            return

        if messagebox.askyesno("Confirm", "Do you confirm your order?"):
            self.on_order_callback(name, self.order_details)
            self.order_ready_message()
        else:
            messagebox.showinfo("Order", "Order cancelled.")

    def order_ready_message(self):
        messagebox.showinfo("Order", "Your order is ready!")
        self.root.quit()  # Закрытие приложения
    def show_information(self):
        information = ["Author - Agonek", "Language - Python", "Day of release - 27/04/24"]
        str_info = "\n".join(information)
        messagebox.showinfo("Information", str_info)

    def finish(self):
        self.root.destroy()
        print("App is closing...")

    def temporary_decision(self):
        pass

    def clearing(self):
        pass