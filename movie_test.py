import unittest
from movie import Movie, REGULAR, CHILDREN, NEW_RELEASE


class MovieTest(unittest.TestCase):
    def test_instance(self):
        self.movie1 = Movie('one', NEW_RELEASE)
        self.movie2 = Movie('two', REGULAR)
        self.movie3 = Movie('three', CHILDREN)
        self.movie4 = Movie('four', CHILDREN)

        self.assertNotEqual(self.movie1.price_code, self.movie2.price_code)
        self.assertEqual(self.movie3.price_code, self.movie4.price_code)