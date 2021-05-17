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

class Customer:

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        self.basket = basket()

    @property
    def basket(self):
        return _basket

    @basket.setter
    def basket(self, new_basket):
        self._basket = new_basket

    @property
    def age(self):
        return _calculate_age()

    def _calculate_age(self):
        diff = date.today() - self.birthdate
        return round(diff.days / 365, 1)

    def add_to_basket(self, item):
        if isinstance(item, Item):
            if item.is_allowed(self.age):
                self._basket.add(item)
            else:
                raise ValueError(f"Cannot purchase '{item.name}', you haven't reach the age limit!")
        else:
            raise TypeError(f"Can add only instances of class 'Item'")

    def remove_to_basket(self, item):
        if isinstance(item, Item):
            self._basket.remove(item)
        else:
            raise TypeError(f"Can remove only instances of class 'Item'")










