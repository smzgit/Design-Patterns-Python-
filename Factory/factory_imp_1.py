from abc import ABC, abstractmethod


class Burger(ABC):
    price = 0

    @abstractmethod
    def ingredients(self):
        pass

    @abstractmethod
    def type_of_burger(self):
        pass

    @abstractmethod
    def burger_price(self):
        pass


class VegBurger(Burger):
    price = 80

    def ingredients(self):
        print(f'Ingredients = 2 buns, 1 mixed veg pattie, 2 tomato slices, 2 cucumber slices, mayo, ketchup')

    def type_of_burger(self):
        print(f'Im a  simple veg burger')

    def burger_price(self):
        print(f'Veg burger price = Rs. {VegBurger.price}')


class VegCheeseBurger(Burger):
    price = 120

    def ingredients(self):
        print(
            f'Ingredients = 2 buns, 2 mixed veg pattie,2 Cheese slices, 2 tomato slices, 2 cucumber slices, mayo, ketchup')

    def type_of_burger(self):
        print(f'Im a  Cheese veg burger')

    def burger_price(self):
        print(f'Cheese veg burger price = Rs. {VegCheeseBurger.price}')


class NonVegBurger(Burger):
    price = 150

    def ingredients(self):
        print(
            f'Ingredients = 2 buns, 1 chicken pattie,2 Cheese slices, 2 tomato slices, 2 cucumber slices, mayo, ketchup & mustard sauce')

    def type_of_burger(self):
        print(f'Im a  Non veg burger')

    def burger_price(self):
        print(f'Non veg burger price = Rs. {NonVegBurger.price}')


class BurgerFactory(ABC):
    @abstractmethod
    def get_burger(self) -> Burger:
        pass


class VegBurgerMaker(BurgerFactory):
    def get_burger(self) -> Burger:
        return VegBurger()


class VegCheeseBurgerMaker(BurgerFactory):
    def get_burger(self) -> Burger:
        return VegCheeseBurger()


class NonVegBurgerMaker(BurgerFactory):
    def get_burger(self) -> Burger:
        return NonVegBurger()


if __name__ == '__main__':
    all_burgers = dict(veg=VegBurgerMaker(),cheeseveg=VegCheeseBurgerMaker(),nonveg=NonVegBurgerMaker)
    while True:
        type = input("enter  the type of burger you want - \n1. veg\n2. cheeseveg\n3. nonveg\n4. exit\n> ")
        if type=='exit':
            exit()
        if type in all_burgers:
            burgerfactory = all_burgers[type]
            burger = burgerfactory.get_burger()
            burger.type_of_burger()
            burger.burger_price()
            burger.ingredients()
        else:
            print('wrong input value, renter again..\n')
            