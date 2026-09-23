class Herbivore:
    def eat_plants(self):
        print("Eats plants")


class Carnivore:
    def eat_meat(self):
        print("Eats meat")


class Omnivore:
    def eat_both(self):
        print("Eats both plants and meat")


class Bear(Herbivore, Carnivore, Omnivore):
    def show(self):
        print("Bear is an omnivore")


bear = Bear()

bear.show()
bear.eat_plants()
bear.eat_meat()
bear.eat_both()