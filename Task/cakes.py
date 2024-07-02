
import random
import Beautiful_terminal as bt

from os import system
from time import sleep



class Oven:
    def __init__(self, name):
        self.name = name
        self.case = {"Chocolate Cake": {"Small": 0, "Medium": 0, "Large": 0},
                      "Vanilla Cake": {"Small": 0, "Medium": 0, "Large": 0},
                        "Strawberry Cake": {"Small": 0, "Medium": 0, "Large": 0},
                          "Birthday Cake": {"Small": 0, "Medium": 0, "Large": 0},
                            "Gluten-free Cake": {"Small": 0, "Medium": 0, "Large": 0},
                              "Vegan Cake": {"Small": 0, "Medium": 0, "Large": 0}}

    def bake_cake(self):
        pass


class Cake:
    def __init__(self, name, type, size, price, ingredients):
        self.name = name
        self.type = type
        self.size = size
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}: {self.ingredients}"

    def creat_cake(self):
        cake_size = random.choice(["Small", "Medium", "Large"])
        if cake_size == "Small":
            cake_price = 15
        elif cake_size == "Medium":
            cake_price = 25
        else:
            cake_price = 40
    
        CHOCOLATE_CAKES = Cake("Chocolate Cake", "Regular", cake_size, cake_price, ["chocolate", "flour", "sugar", "eggs"])
        VANILLA_CAKES = Cake("Vanilla Cake", "Regular", cake_size, cake_price, ["flour", "sugar", "eggs", "vanilla extract"])
        STRAWBERRY_CAKES = Cake("Strawberry Cake", "Regular", cake_size, cake_price, ["flour", "sugar", "eggs", "strawberries"])
        BIRTHDAY_CAKES= Cake("Birthday Cake", "Special", cake_size, cake_price, ["chocolate", "vanilla", "cream", "candles"])
        GLUTEN_FREE_CAKES = Cake("Gluten-free Cake", "Special", cake_size, cake_price, ["gluten-free flour", "sugar", "eggs", "vanilla extract"])
        VEGAN_CAKES = Cake("Vegan Cake", "Special", cake_size, cake_price, ["flour", "sugar", "vegan eggs", "vanilla extract"])

        self.list_of_cakes_recipes = [CHOCOLATE_CAKES, VANILLA_CAKES, STRAWBERRY_CAKES, BIRTHDAY_CAKES, GLUTEN_FREE_CAKES, VEGAN_CAKES]


def show_list_of_cakes_recipes():
    list_of_cakes = [[x.name, x.ingredients] for x in Cake.list_of_cakes]
    print("Your list of cake recipes:")
    for num, cake in enumerate(list_of_cakes, 1):
        print("{}. {} {}".format(num, *cake))


def main():
    pass
    

if __name__ == "__main__":
    main()
