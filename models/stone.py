from abc import ABC, abstractmethod


class Stone(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def get_full_price(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}"


class PreciousStone(Stone):
    def __init__(self, name, color, carat, clarity, price_per_carat):
        super().__init__(name, color)
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat

    def get_full_price(self):
        return self.price_per_carat * self.carat

    def increase_clarity(self):
        self.clarity += 1

    def increase_price(self, percentage):
        self.price_per_carat += (self.price_per_carat * percentage) / 100

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Carat: {self.carat}," \
               f" Clarity: {self.clarity}, Price per Carat: {self.price_per_carat}"


class ArtificialPreciousStone(Stone):
    def __init__(self, name, color, lab_name, weight_grams, price_per_gram):
        super().__init__(name, color)
        self.lab_name = lab_name
        self.weight_grams = weight_grams
        self.price_per_gram = price_per_gram

    def get_full_price(self):
        return self.price_per_gram * self.weight_grams

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Lab Name: {self.lab_name}, " \
               f"Weight (grams): {self.weight_grams}, Price per Gram: {self.price_per_gram}"


class Minerals(Stone):
    def __init__(self, name, color, weight_grams, cost, price_per_gram):
        super().__init__(name, color)
        self.weight_grams = weight_grams
        self.cost = cost
        self.price_per_gram = price_per_gram

    def get_full_price(self):
        return self.price_per_gram * self.weight_grams

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Weight_grams: {self.weight_grams}," \
               f" Cost: {self.cost}, Price per gram: {self.price_per_gram}"
