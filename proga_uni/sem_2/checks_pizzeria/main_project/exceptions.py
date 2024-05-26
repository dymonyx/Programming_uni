class CheeseException(BaseException):
    """Класс исключения при отсутствии сыра в пицце"""


class DoughException(BaseException):
    """Класс исключения для несуществующих видов пицц"""


class CorrectNumb(Exception):
    pass


class NotExistProduct(Exception):
    """Класс исключения для добавления несуществующего товара"""


class OrderIsNotEmpty(Exception):
    pass


def counting(order_list):
    if len(order_list) != 0:
        raise OrderIsNotEmpty
    else:
        return
