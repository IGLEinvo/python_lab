"""
Module containing the ArtificialPreciousStone class.
"""

from models.stone import Stone  # pylint: disable = import-error


class ArtificialPreciousStone(Stone):
    """
    Concrete subclass representing artificial precious stones, derived from the Stone class.

    Attributes:
        name (str): The name of the artificial precious stone.
        color (str): The color of the artificial precious stone.
        lab_name (str): The name of the laboratory where the stone was created.
        weight (float): The weight of the artificial precious stone in grams.
        price_per_gram (float): The price per gram of the artificial precious stone.

    Methods:
        get_full_price(): Calculates the full price of the artificial precious stone.
        __str__(): Returns a string representation of the artificial precious stone.

    Example Usage:
        stone = ArtificialPreciousStone("Cubic Zirconia", "Clear", "XYZ Lab", 3.5, 50)
        print(stone)
    """

    def __init__(self, name, color, lab_name, weight, price_per_gram):  # pylint: disable= too-many-arguments
        """
        Initializes a new instance of the ArtificialPreciousStone class.

        Args:
            name (str): The name of the artificial precious stone.
            color (str): The color of the artificial precious stone.
            lab_name (str): The name of the laboratory where the stone was created.
            weight (float): The weight of the artificial precious stone in grams.
            price_per_gram (float): The price per gram of the artificial precious stone.
        """
        super().__init__(name, color)
        self.lab_name = lab_name
        self.weight = weight
        self.price_per_gram = price_per_gram

    def get_attributes_by_type(self, data_type):
        attributes = {attr: value for attr, value in self.__dict__.items() if isinstance(value, data_type)}
        print(f"Attributes of type {data_type}:")
        for attr, value in attributes.items():
            print(f"{attr}: {value}")
        return attributes

    def get_full_price(self):
        """
        Calculates the full price of the artificial precious stone.

        Returns:
            float: The full price of the artificial precious stone.
        """
        return self.price_per_gram * self.weight

    def calculate_value(self):
        return self.weight * self.price_per_gram

    def __str__(self):
        """
        Returns a string representation of the artificial precious stone.

        Returns:
            str: String representation of the artificial precious stone.
        """

        return (
            f"Name: {self.name}, Color: {self.color}, Lab Name: {self.lab_name}, "
            f"Weight (grams): {self.weight}, Price per Gram: {self.price_per_gram}"
        )
