class Terminal:
    def __init__(self, menu=['PizzaPepperoni', 'PizzaBarbeque', 'PizzaSeafood']):
        self._menu = menu

    def get_menu(self):
        return ','.join(self._menu)

    def start_work(self):
        name = input('What is your name? ')
        print(*self._menu)
        action = input('What would you like to order? ')
        order = Order(name)
        while action != 'Q':
            size = input("What size would you like to order? (30cm, 35cm, 40cm) ")
            if action == 'PizzaPepperoni':
                if len(order.order_list) != 0:
                    pepperoni_pizzas = len([pizza for pizza in order.order_list if 'PizzaPepperoni' in str(pizza)])
                else:
                    pepperoni_pizzas = 0
                order.order_list.append(PizzaPepperoni(f"PizzaPepperoni_{pepperoni_pizzas + 1}_" + size, size))
            if action == 'PizzaBarbeque':
                if len(order.order_list) != 0:
                    barbeque_pizzas = len([pizza for pizza in order.order_list if 'PizzaBarbeque' in str(pizza)])
                else:
                    barbeque_pizzas = 0
                order.order_list.append(PizzaBarbeque(f"PizzaBarbeque_{barbeque_pizzas + 1}_" + size, size))
            if action == 'PizzaSeafood':
                if len(order.order_list) != 0:
                    seafood_pizzas = len([pizza for pizza in order.order_list if "PizzaSeafood" in str(pizza)])
                else:
                    seafood_pizzas = 0
                order.order_list.append(PizzaSeafood(f"PizzaSeafood_{seafood_pizzas + 1}_" + size, size))
            action = input('Do you want to add more pizzas? yes/no: ')
            if action == 'yes':
                print(*self._menu)
                action = input('What would you like to order? ')
            else:
                break
        if len(order.order_list) != 0:
            answer = input('Do you confirm your order? yes/no: ')
            if answer == 'yes':
                order.get_price()
                print('Thanks for ordering! See you next time!')
            else:
                print('See you next time!')
        else:
            print('See you next time!')
        del order
