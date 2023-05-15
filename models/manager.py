from models.stone import Stone, PreciousStone


class StoneManager:
    def __init__(self):
        self.stones = []

    def add_stone(self, stone):
        self.stones.append(stone)

    def display_stones(self):
        for stone in self.stones:
            print(stone)


# Main method
if __name__ == "__main__":
    stone_manager = StoneManager()
    stone1 = Stone("Emerald", "Green")
    stone2 = Stone("Sapphire", "Blue")
    stone3 = PreciousStone("Diamond", "White", 2.5, 5, 1000)
    stone_manager.add_stone(stone1)
    stone_manager.add_stone(stone2)
    stone_manager.add_stone(stone3)
    stone_manager.display_stones()
