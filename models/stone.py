"""
Module containing the Stone class.
"""

from abc import ABC, abstractmethod


# pylint: disable = import-error
class Stone(ABC):
    """
    Abstract base class representing a stone.

    Attributes:
        name (str): The name of the stone.
        color (str): The color of the stone.

    Methods:
        get_full_price(): Abstract method to calculate the full price of the stone.
        __str__(): Returns a string representation of the stone.

    Example Usage:
        class Diamond(Stone):
            def __init__(self, name, color, carat, price_per_carat):
                super().__init__(name, color)
                self.carat = carat
                self.pricePerCarat = price_per_carat

            def get_full_price(self):
                return self.carat * self.pricePerCarat

            def __str__(self):
                return f"Name: {self.name}, Color: {self.color},
                 Carat: {self.carat}, Price per Carat: {self.pricePerCarat}"

        diamond = Diamond("Diamond", "White", 2.5, 1000)
        print(diamond)
    """

    def __init__(self, name, color):
        """
        Initializes a new instance of the Stone class.

        Args:
            name (str): The name of the stone.
            color (str): The color of the stone.
        """
        self.name = name
        self.color = color
        self.attribute_set = set()

    @abstractmethod
    def get_full_price(self):
        """
        Abstract method to calculate the full price of the stone.
        """

    def __str__(self):
        """
        Returns a string representation of the stone.

        Returns:
            str: String representation of the stone.
        """
        return f"Name: {self.name}, Color: {self.color}"

    def __iter__(self):
        return iter(self.attribute_set)
