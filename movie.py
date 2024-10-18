import logging
from pricing import Regular, NewRelease, Children, PriceStrategy

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

    def get_price_code(self):
        return self.price_code

    def get_price(self, days):
        return self.price_code.get_price(days)

    def get_rental_points(self, days):
        return self.price_code.get_rental_points(days)
