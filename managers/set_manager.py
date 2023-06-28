from managers.stone_manager import StoneManager
from models.artificial_precious_stone import ArtificialPreciousStone
from models.minerals import Minerals
from models.precious_stone import PreciousStone


def log_narguments(func):
    def wrapper(*args, **kwargs):
        with open('кількість аргументів(SM).txt', 'a') as file:
            file.write(f"Метод: {func.__name__}\n")
            file.write(f"Кількість аргументів: {len(args) + len(kwargs)}\n")
        return func(*args, **kwargs)

    return wrapper


def log_arguments(func):
    def wrapper(*args, **kwargs):
        with open('Клас_метод_результат(Set_manager).txt', 'a') as file:
            file.write(f"{func.__name__}:\n")
            for arg in args:
                file.write(f"arg={arg}\n")
            for arg, value in kwargs.items():
                file.write(f"{arg}={value}\n")
            result = func(*args, **kwargs)
        return result

    return wrapper


class SetManager:
    @log_narguments
    @log_arguments
    def __init__(self, regular_manager):
        self.regular_manager = regular_manager

    @log_narguments
    @log_arguments
    def generate_attributes(self):
        for stone in self.regular_manager.stones:
            for attribute in stone.__dict__.values():
                yield attribute


if __name__ == "__main__":
    minerals = Minerals("Minerals", "Blue", {"rock", "crystal"}, 100, 0.5)
    precious_stone = PreciousStone("Precious Stone", "Red", {"gem", "sparkling"}, "SI1", 1000, 2.5)
    artificial_precious_stone = ArtificialPreciousStone("Artificial Stone", "Green", {"synthetic", "shiny"}, 1.0, 0.2)

    stone_manager = StoneManager()
    stone_manager.add_stone(minerals)
    stone_manager.add_stone(precious_stone)
    stone_manager.add_stone(artificial_precious_stone)

    set_manager = SetManager(stone_manager)

    for attribute in set_manager.generate_attributes():
        print(attribute)