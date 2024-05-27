class Order:
    def __init__(self, name, order_list=[]):
        self._name = name
        self.order_list = order_list

    def __repr__(self):
        return self._name

    @property
    def name(self):
        return self._name

    def get_price(self):
        final_price = 0
        for pizza in self.order_list:
            if 'Pepperoni' in str(pizza):
                price = 10
            elif 'Barbeque' in str(pizza):
                price = 13
            else:
                price = 15
            if "30cm" in str(pizza):
                final_price += price
            elif '35cm' in str(pizza):
                final_price += int(price * 1.3)
            else:
                final_price += int(price * 1.5)
        pizzas = [str(pizza) for pizza in self.order_list]
        print(f"Your order contains: {','.join(pizzas)} and final price is {final_price}")
        return final_price
