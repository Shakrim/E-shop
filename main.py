from datetime import date

class Item:
    """
    This class represents an item in the basket.
    """
    def __init__(self, name:str, price:int, age_limit = 0):
        self.name = name
        self.price = price
        self.age_limit = age_limit

    def is_allowed(self, customer_age:int) -> bool:
        """
        This method makes the decision of adding the new item into basket based on the age of customer.
        """
        return customer_age >= self.age_limit


class Basket:
    """
    This class represents the shopping basket.
    """
    def __init__(self):
        self.__items = []
        self.discount = 0

    @property
    def total_price(self):
        return round(sum([item.price for item in self.__items])) * (1 - self._discount)

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount (self, discount):
        self._discount = discount

    def add(self, item):
        self.__items.append(item)

    def remove(self, item):
        self.__items.remove(item)

# class Customer:
#
#     def __init__(self,):
#         self.name = name
#         self.bi






