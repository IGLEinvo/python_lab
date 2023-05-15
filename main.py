class PreciousStone:
    instance = None

    def __init__(self, name, carat, color, clarity, price_per_carat):
        self.name = name
        self.carat = carat
        self.color = color
        self.clarity = clarity
        self.pricePerCarat = price_per_carat

    def get_total_price(self):
        return self.pricePerCarat * self.carat

    def increase_clarity(self):
        self.clarity += 1

    def increase_price(self, percentage):
        self.pricePerCarat += (self.pricePerCarat * percentage) / 100

    @staticmethod
    def get_instance():
        if not PreciousStone.instance:
            PreciousStone.instance = PreciousStone("Default", 0, "Default", 0, 0)
        return PreciousStone.instance


# Main method
if __name__ == "__main__":
    stone1 = PreciousStone("Diamond", 2.5, "White", 5, 1000)
    stone2 = PreciousStone("Ruby", 1.8, "Red", 6, 800)
    stone3 = PreciousStone.get_instance()
    stone4 = PreciousStone.get_instance()

    stones = [stone1, stone2, stone3, stone4]
    for stone in range(len(stones)):
        print("Object ID:", id(stones[stone]))
