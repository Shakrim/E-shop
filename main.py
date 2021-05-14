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
        self.discount = discount

    @property





