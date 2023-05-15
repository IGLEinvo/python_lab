from models.stone import PreciousStone, ArtificialPreciousStone, Minerals


class StoneManager:
    def __init__(self):
        self.stones = []

    def add_stone(self, stone):
        self.stones.append(stone)

    def find_stone_by_name(self, name):
        return list(filter(lambda s: s.name == name, self.stones))

    def find_stone_by_color(self, color):
        return list(filter(lambda s: s.color == color, self.stones))

    def display_stones(self):
        for stone in self.stones:
            print(stone)


# Main method
if __name__ == "__main__":
    stone_manager = StoneManager()
    stone1 = Minerals("Peat", "Brown", 20, 10, 600)
    stone2 = Minerals("Rock salt", "colorless", 10, 5, 1)
    stone3 = PreciousStone("Diamond", "White", 2.5, 5, 1000)
    stone4 = PreciousStone("Ruby", "Red", 1.8, 6, 800)
    stone5 = ArtificialPreciousStone("Lab Diamond", "White", "ABC Lab", 3.2, 1500)
    stone6 = ArtificialPreciousStone("Lab Ruby", "Red", "XYZ Lab", 2.1, 1200)

    stone_manager.add_stone(stone1)
    stone_manager.add_stone(stone2)
    stone_manager.add_stone(stone3)
    stone_manager.add_stone(stone4)
    stone_manager.add_stone(stone5)
    stone_manager.add_stone(stone6)

    print("Stones:")
    stone_manager.display_stones()

    print("\nSearching for stones:")
    name_results = stone_manager.find_stone_by_name("Diamond")
    print("Stones with name 'Diamond':")
    for stone in name_results:
        print(stone)

    color_results = stone_manager.find_stone_by_color("Red")
    print("\nStones with color 'Red':")
    for stone in color_results:
        print(stone)
