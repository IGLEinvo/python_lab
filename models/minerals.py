"""
Module containing the Minerals class.
"""

from models.stone import Stone  # pylint: disable = import-error


class Minerals(Stone):
    """
    Concrete subclass representing minerals, derived from the Stone class.

    Attributes:
        name (str): The name of the mineral.
        color (str): The color of the mineral.
        weight (float): The weight of the mineral in grams.
        cost (float): The cost of the mineral.
        price_per_gram (float): The price per gram of the mineral.

    Methods:
        get_full_price(): Calculates the full price of the mineral.
        __str__(): Returns a string representation of the mineral.

    Example Usage:
        mineral = Minerals("Quartz", "Transparent", 50, 100, 2)
        print(mineral)
    """

    def __init__(self, name, color, weight, cost, price_per_gram):  # pylint: disable= too-many-arguments
        """
        Initializes a new instance of the Minerals class.

        Args:
            name (str): The name of the mineral.
            color (str): The color of the mineral.
            weight (float): The weight of the mineral in grams.
            cost (float): The cost of the mineral.
            price_per_gram (float): The price per gram of the mineral.
        """
        super().__init__(name, color)
        self.weight = weight
        self.cost = cost
        self.price_per_gram = price_per_gram

    def get_attributes_by_type(self, data_type):
        attributes = {attr: value for attr, value in self.__dict__.items() if isinstance(value, data_type)}
        print(f"Attributes of type {data_type}:")
        for attr, value in attributes.items():
            print(f"{attr}: {value}")
        return attributes

    def get_full_price(self):
        """
        Calculates the full price of the mineral.

        Returns:
            float: The full price of the mineral.
        """
        return self.price_per_gram * self.weight

    def calculate_value(self):
        return self.weight * self.price_per_gram

    def __str__(self):
        """
        Returns a string representation of the mineral.

        Returns:
            str: String representation of the mineral.
        """
        return (
            f"Name: {self.name}, Color: {self.color}, Weight_grams: {self.weight},"
            f" Cost: {self.cost}, Price per gram: {self.price_per_gram}"
        )
