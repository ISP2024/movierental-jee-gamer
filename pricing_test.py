import unittest
from movie import Movie
from datetime import datetime
from rental import Rental

from pricing import Regular, NewRelease, Children


class PriceTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("new", datetime.now().year, "default")
        self.children_movie = Movie("child", 1990, "Children")
        self.regular_movie = Movie("average", 1990, "Legacy")

    def test_all_movie(self):
        movie_code = Rental.price_code_for_movie(self.new_movie)
        self.assertEqual(movie_code, NewRelease())

        movie_code = Rental.price_code_for_movie(self.children_movie)
        self.assertEqual(movie_code, Children())

        movie_code = Rental.price_code_for_movie(self.regular_movie)
        self.assertEqual(movie_code, Regular())
