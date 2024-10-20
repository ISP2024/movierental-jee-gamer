import logging
from datetime import datetime
from pricing import Regular, NewRelease, Children, PriceStrategy

REGULAR = Regular()
NEW_RELEASE = NewRelease()
CHILDREN = Children()


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie, days_rented):
        """
        Initialize a new movie rental object for
        a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = self.price_code_for_movie(movie)

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        return self.price_code.get_price(self.days_rented)

    def get_rental_points(self):
        return self.price_code.get_rental_points(self.days_rented)

    def get_price_code(self):
        return self.price_code

    @classmethod
    def price_code_for_movie(cls, movie):
        if movie.year == datetime.now().year:
            return NEW_RELEASE

        if "Children" in movie.genre or "Childrens" in movie.genre:  # But if a tag has Children in it but is not a children movie then it would be wrong
            return CHILDREN

        return REGULAR


