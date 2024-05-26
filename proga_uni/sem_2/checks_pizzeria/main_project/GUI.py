import subprocess
from tkinter import *
from tkinter import ttk, messagebox

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

        ttk.Button(text="Show Ingredients", command=self.show_ingredients).grid(row=3, column=1)
        ttk.Button(text="Add one more pizza", command=self.add_pizza).grid(row=4, column=1)
        ttk.Button(text="Show Order", command=self.show_order).grid(row=5, column=1)
        ttk.Button(text="Order", command=self.finalize_order).grid(row=6, column=1)

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

    def show_ingredients(self):
        if not self.order_details:
            messagebox.showerror("Error", "No pizzas in the order.")
            return

        # Создаем новое окно для изменения ингредиентов выбранной пиццы
        ingredients_window = Toplevel(self.root)
        ingredients_window.title("Show Ingredients")
        ingredients_window.geometry("400x300")

        pizza_listbox = Listbox(ingredients_window)
        pizza_listbox.pack(fill=BOTH, expand=True)

        for idx, detail in enumerate(self.order_details):
            pizza_listbox.insert(END, f"{idx+1}. {detail['action']} - {detail['size']}")

        def select_pizza(event):
            try:
                selected_index = pizza_listbox.curselection()[0]
                selected_pizza = self.order_details[selected_index]
            except  IndexError:
                pass

            # Удаляем предыдущее окно с ингредиентами
            try:
                for widget in ingredients_window.winfo_children():
                    widget.destroy()
            except:
                pass

            # Создаем новое окно с ингредиентами для выбранной пиццы
            ingredients_window = Toplevel(self.root)
            ingredients_window.title("Change Ingredients")
            ingredients_window.geometry("400x300")

            ingredients_label = Label(ingredients_window, text="Ingredients:")
            ingredients_label.pack()

            ingredients_listbox = Listbox(ingredients_window, selectmode=MULTIPLE)
            ingredients_listbox.pack(fill=BOTH, expand=True)

            try:
                for ingredient in selected_pizza['ingredients']:
                    ingredients_listbox.insert(END, ingredient)
            except UnboundLocalError:
                pass
        pizza_listbox.bind('<<ListboxSelect>>', select_pizza)

    def add_pizza(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        if not self.pizza_var.get() or not self.size_var.get():
            messagebox.showerror("Error", "Please select a pizza and size.")
            return
        if self.pizza_var.get() in "Pepperoni":
            ingredients_to_change = ['cheese', 'pepperoni', 'italian_herbs']
        elif self.pizza_var.get() in "Barbeque":
            ingredients_to_change = ['cheese', 'sauce barbeque', 'bacon', 'tomatoes', 'eggplant', 'champignons', 'sweet onions',
                           'pickles', 'parsley']
        else:
            ingredients_to_change = ['cheese', 'calamari', 'shrimp', 'mussels', 'octopus', 'tomatoes', 'red pepper']

        self.order_details.append({
            'action': self.pizza_var.get(),
            'size': self.size_var.get(),
            'ingredients': ingredients_to_change
        })
        messagebox.showinfo("Success", f"Added {self.pizza_var.get()} of size {self.size_var.get()}")

        # Reset selection
        self.pizza_var.set("")
        self.size_var.set("")

    def show_order(self):
        if not self.order_details:
            messagebox.showerror("Error", "No pizzas in the order.")
            return

        order_summary = "\n".join([f"{detail['action']} - {detail['size']}" for detail in self.order_details])
        messagebox.showinfo("Order Summary", order_summary)

    def finalize_order(self):
        name = self.name_entry.get()
        if not self.order_details:
            messagebox.showerror("Error", "No pizzas in the order.")
            return

        if messagebox.askyesno("Confirm", "Do you confirm your order?"):
            # добавить тут окно где будет выводиться инфа о приготовлении или просто выкидывать инфу в меню
            self.on_order_callback(name, self.order_details)
            self.order_ready_message()
        else:
            messagebox.showinfo("Order", "Order cancelled.")
            self.root.quit()  # Закрытие приложения

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
        self.order_details = []
        self.pizza_var.set("")
        self.size_var.set("")
        self.name_entry.delete(0, END)
        messagebox.showinfo("Info", "All data has been cleared.")


'''
    def show_waiting_list(self):
        waiting_list_window = Toplevel(self.root)
        waiting_list_window.title("Waiting List")

        info_text = Text(waiting_list_window, height=20, width=80)
        info_text.pack()

        # Сохраняем стандартный вывод в переменную для дальнейшего использования
        original_stdout = sys.stdout

        # Перенаправляем стандартный вывод в StringIO
        sys.stdout = StringIO()

        def update_text():
            info_text.delete(1.0, END)  # Очистка текстового поля
            info_text.insert(END, sys.stdout.getvalue())  # Вставка текущего значения StringIO
            info_text.see(END)  # Прокрутка вниз
            self.root.after(1000, update_text)  # Обновление каждые 1000 мс

        # Восстанавливаем стандартный вывод при закрытии окна
        def on_close():
            sys.stdout = original_stdout
            waiting_list_window.destroy()

        waiting_list_window.protocol("WM_DELETE_WINDOW", on_close)

        # Запуск обновления текста
        update_text()
'''


