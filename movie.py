import logging
from collections import Collection
from typing import Optional
import csv

class MovieCatalog:
    _instance = None


    def __init__(self):
        self.movie = []
        with open('data/movies.csv', newline='') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                movie = Movie(row['title'], row['year'], row['genres'])
                movieID = row['#id']
                # Do your stuff

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    def get_movie(self, title: str, year: Optional[int] = None):
        # get movie with same stuff

class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str, year: int, genre: Collection[str]):
        # Initialize a new movie. 
        self.__title = title
        self.__year = year
        self.__genre = genre

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @property
    def genre(self):
        return self.__genre

    def __str__(self):
        return f"{self.title} ({self.year})"

    def is_genre(self, genre: str):
        that_genre = genre.lower()
        return that_genre in self.__genre


