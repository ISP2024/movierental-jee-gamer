import unittest
from customer import Customer
from rental import Rental
from movie import Movie, REGULAR, NEW_RELEASE, CHILDREN


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", NEW_RELEASE)
        self.regular_movie = Movie("Air", REGULAR)
        self.childrens_movie = Movie("Frozen", CHILDREN)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", REGULAR)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(REGULAR, m.price_code)

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

