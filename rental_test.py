import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from datetime import datetime


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", datetime.now().year, "new")
        self.regular_movie = Movie("Air", 2000, "air")
        self.childrens_movie = Movie("Frozen", 2000, "Children")

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2000, "air")
        self.assertEqual("Air", m.title)
        self.assertEqual(2000, m.year)

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_price(), 3.5)

        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3.0)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)

        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_rental_points(), 1)

        rental = Rental(self.childrens_movie, 2)
        self.assertEqual(rental.get_rental_points(), 1)

