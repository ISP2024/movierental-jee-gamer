import logging
from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""

    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    def get_price(self, days: int) -> float:
        return 3 * days

    def get_rental_points(self, days: int) -> int:
        return days


class Regular(PriceStrategy):
    def get_price(self, days: int) -> float:
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days: int) -> int:
        return 1


class Children(PriceStrategy):
    def get_price(self, days: int) -> float:
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days: int) -> int:
        return 1


REGULAR = Regular()
NEW_RELEASE = NewRelease()
CHILDREN = Children()


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, price_code: PriceStrategy):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_price(self, days):
        return self.price_code.get_price(days)

    def get_rental_points(self, days):
        return self.price_code.get_rental_points(days)
