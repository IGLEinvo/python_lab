from models.artificial_precious_stone import ArtificialPreciousStone
from models.minerals import Minerals
from models.precious_stone import PreciousStone
import logging

logging.basicConfig(filename='exception.txt', level=logging.ERROR)


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except exception as e:
                if mode == "console":
                    logging.error(str(e))
                elif mode == "file":
                    logging.error(str(e), exc_info=True)
                else:
                    raise ValueError("Invalid logging mode. Supported modes: 'console', 'file'")
                raise

        return wrapper

    return decorator


class RedundantWeightException(Exception):
    def __init__(self, weight):
        self.weight = weight
        super().__init__(f"Redundant weight: {weight}")


def log_narguments(func):
    def wrapper(*args, **kwargs):
        with open('кількість аргументів(StoneM).txt', 'a') as file:
            file.write(f"Метод: {func.__name__}\n")
            file.write(f"Кількість аргументів: {len(args) + len(kwargs)}\n")
        return func(*args, **kwargs)

    return wrapper


def log_arguments(func):
    def wrapper(*args, **kwargs):
        with open('Клас_метод_результат(Stone_manager).txt', 'a') as file:
            file.write(f"{func.__name__}:\n")
            for arg in args:
                file.write(f"arg={arg}\n")
            for arg, value in kwargs.items():
                file.write(f"{arg}={value}\n")
            result = func(*args, **kwargs)
        return result

    return wrapper


class StoneManager:
    def __init__(self):
        self.stones = []

    def __len__(self):
        return len(self.stones)

    def __getitem__(self, index):
        return self.stones[index]

    def __iter__(self):
        return iter(self.stones)

    @log_arguments
    @logged(RedundantWeightException, "file")
    @log_narguments
    def add_stone(self, stone):
        if stone.weight == 0:
            raise RedundantWeightException(stone.weight)
        self.stones.append(stone)

    @log_narguments
    def find_stone_by_name(self, name):
        return list(filter(lambda s: s.name == name, self.stones))

    @log_narguments
    def find_stone_by_color(self, color):
        return list(filter(lambda s: s.color == color, self.stones))

    @log_narguments
    @logged(RedundantWeightException, "file")
    def display_stones(self):
        for stone in self.stones:
            print(stone)

    @log_narguments
    def get_stones_by_attribute(self, attribute):
        values = []
        for stone in self.stones:
            if isinstance(stone, Minerals) and attribute == "weight":
                values.append(stone.weight)
            elif isinstance(stone, PreciousStone) and attribute == "carat":
                values.append(stone.carat)
            elif isinstance(stone, ArtificialPreciousStone) and attribute == "weight_grams":
                values.append(stone.weight)
        return values

    @logged(RedundantWeightException, "file")
    def check_condition(self, condition):
        all_satisfy = all(condition(stone) for stone in self.stones)
        any_satisfy = any(condition(stone) for stone in self.stones)
        return {"all": all_satisfy, "any": any_satisfy}

    @logged(RedundantWeightException, "file")
    def enumerate_stones(self):
        enumerated_stones = [(index, stone) for index, stone in enumerate(self.stones)]
        return enumerated_stones

    @logged(RedundantWeightException, "file")
    def zip_stones_with_method(self, method):
        zipped_stones = [(stone, method(stone)) for stone in self.stones]
        return zipped_stones

    @logged(RedundantWeightException, "file")
    def get_attributes_by_type(self, data_type, print_attributes=False):
        attributes = {}
        for stone in self.stones:
            if hasattr(stone, 'get_attributes_by_type'):
                stone_attributes = stone.get_attributes_by_type(data_type)
                attributes.update(stone_attributes)
                if print_attributes:
                    print(f"Attributes of {stone.name}:")
                    for attr, value in stone_attributes.items():
                        print(f"{attr}: {value}")
                    print()
        return attributes


if __name__ == "__main__":
    stone_manager = StoneManager()
    stone1 = Minerals("Peat", "Brown", 20, 10, 600)
    stone2 = Minerals("Rock salt", "colorless", 10, 5, 1)
    stone3 = PreciousStone("Diamond", "White", 2.5, 5, 1000, 12)
    stone4 = PreciousStone("Ruby", "Red", 1.8, 6, 800, 11)
    stone5 = ArtificialPreciousStone("Lab's Diamond", "White", "ABC Lab", 3.2, 1500)
    stone6 = ArtificialPreciousStone("Lab's Ruby", "Red", "XYZ Lab", 2.1, 1200)

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

    print("\nGetting stone weights:")
    stone_weights = stone_manager.get_stones_by_attribute("weight")
    print(stone_weights)

    print("\nEnumerating stones:")
    enumerated_stones = stone_manager.enumerate_stones()
    for index, stone in enumerated_stones:
        print(f"Index: {index}, Stone: {stone}")

    print("\nZipping stones with method:")
    zipped_stones = stone_manager.zip_stones_with_method(lambda s: s.calculate_value())
    for stone, value in zipped_stones:
        print(f"Stone: {stone}, Value: {value}")

    print("\nGetting attributes of type int:")
    attributes_int = stone_manager.get_attributes_by_type(int, print_attributes=True)

    condition1 = lambda stone: isinstance(stone, PreciousStone) and stone.price_per_carat > 700
    condition2 = lambda stone: isinstance(stone, ArtificialPreciousStone) and stone.weight < 5

    result = stone_manager.check_condition(condition1)
    print("All satisfy condition 1:", result["all"])
    print("Any satisfy condition 1:", result["any"])

    result = stone_manager.check_condition(condition2)
    print("All satisfy condition 2:", result["all"])
    print("Any satisfy condition 2:", result["any"])
