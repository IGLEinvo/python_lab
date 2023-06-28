"""
Module containing the PreciousStone class.
"""

from models.stone import Stone  # pylint: disable = import-error


class PreciousStone(Stone):
    """
    Concrete subclass representing precious stones, derived from the Stone class.

    Attributes:
        name (str): The name of the precious stone.
        color (str): The color of the precious stone.
        carat (float): The carat weight of the precious stone.
        clarity (int): The clarity rating of the precious stone.
        price_per_carat (float): The price per carat of the precious stone.

    Methods:
        get_full_price(): Calculates the full price of the precious stone.
        increase_clarity(): Increases the clarity rating of the precious stone.
        increase_price(percentage): Increases the price per carat
        of the precious stone by the given percentage.
        __str__(): Returns a string representation of the precious stone.

    Example Usage:
        stone = PreciousStone("Diamond", "White", 2.5, 5, 1000)
        print(stone)
    """

    def __init__(self, name, color, carat, clarity, price_per_carat, weight):  # pylint: disable= too-many-arguments
        """
        Initializes a new instance of the PreciousStone class.

        Args:
            name (str): The name of the precious stone.
            color (str): The color of the precious stone.
            carat (float): The carat weight of the precious stone.
            clarity (int): The clarity rating of the precious stone.
            price_per_carat (float): The price per carat of the precious stone.
        """
        super().__init__(name, color)
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat
        self.weight = weight

    def get_attributes_by_type(self, data_type):
        attributes = {attr: value for attr, value in self.__dict__.items() if isinstance(value, data_type)}
        print(f"Attributes of type {data_type}:")
        for attr, value in attributes.items():
            print(f"{attr}: {value}")
        return attributes

    def get_full_price(self):
        """
        Calculates the full price of the precious stone.

        Returns:
            float: The full price of the precious stone.
        """
        return self.price_per_carat * self.carat

    def increase_clarity(self):
        """
        Increases the clarity rating of the precious stone by 1.
        """
        self.clarity += 1

    def calculate_value(self):
        return self.weight * self.price_per_carat

    def increase_price(self, percentage):
        """
        Increases the price per carat of the precious stone by the given percentage.

        Args:
            percentage (float): The percentage by which to increase the price per carat.
        """
        self.price_per_carat += (self.price_per_carat * percentage) / 100

    def __str__(self):
        """
        Returns a string representation of the precious stone.

        Returns:
            str: String representation of the precious stone.
        """
        return (
            f"Name: {self.name}, Color: {self.color}, Carat: {self.carat}, "
            f"Clarity: {self.clarity}, Price per Carat: {self.price_per_carat}"
        )
