class Stone:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}"


class PreciousStone(Stone):
    def __init__(self, name, color, carat, clarity, price_per_carat):
        super().__init__(name, color)
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat

    def get_total_price(self):
        return self.price_per_carat * self.carat

    def increase_clarity(self):
        self.clarity += 1

    def increase_price(self, percentage):
        self.price_per_carat += (self.price_per_carat * percentage) / 100

    def get_full_price(self):
        return self.price_per_carat * self.carat

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Carat: {self.carat}, Clarity: {self.clarity}, " \
               f"Price Per Carat: {self.price_per_carat}"


class ArtificialPreciousStone(PreciousStone):
    def __init__(self, name, color, lab_name, weight_grams, price_per_gram):
        super().__init__(name, color, 0, 0, 0)
        self.lab_name = lab_name
        self.weight_grams = weight_grams
        self.price_per_gram = price_per_gram

    def get_full_price(self):
        return self.price_per_gram * self.weight_grams

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Lab Name: {self.lab_name}, " \
               f"Weight in Grams: {self.weight_grams}, " \
               f"Price Per Gram: {self.price_per_gram}"
