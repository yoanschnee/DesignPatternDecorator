from abc import ABC, abstractmethod


class Drink(ABC):

    description : str = None 

    @abstractmethod
    def price(self):
        pass

    def get_description(self):
        return self.description


class Espresso(Drink):

    description = "Espresso"

    def price(self) -> float:
        return 1.20


class DoubleEspresso(Drink):
    
    description = "Double Espresso"

    def price(self) -> float:
        return 2.40
    

class Americano(Drink):

    description = "Americano"

    def price(self) -> float:
        return 3.20
    

class Supplements(Drink):

    _drink : Drink
    description : str

    @abstractmethod
    def price(self):
        pass


class Chocolate(Supplements):

    description = " with Chocolate"

    def __init__(self, drink : Drink) -> None:
        self._drink = drink

    def price(self):
        return self._drink.price() + 0.9
    
    def get_description(self):
        return self._drink.get_description() + self.description


class Vanilla(Supplements):
    
    _drink : Drink = None
    description = " with Vanilla"

    def __init__(self, drink : Drink) -> None:
        self._drink = drink

    def price(self):
        return self._drink.price() + 1.1
    
    def get_description(self):
        return self._drink.get_description() + self.description
    

class Caramel(Supplements):
    
    _drink : Drink = None
    description = " with Caramel"

    def __init__(self, drink : Drink) -> None:
        self._drink = drink

    def price(self):
        return self._drink.price() + 1.0
    
    def get_description(self):
        return self._drink.get_description() + self.description
    

if __name__ == "__main__":
    de = DoubleEspresso()
    de = Chocolate(de)
    de = Vanilla(de)
    de = Caramel(de)
    p = de.price()
    print(de.get_description())
    print(f"The price of a {de.get_description()} is {p} Eur")

     
