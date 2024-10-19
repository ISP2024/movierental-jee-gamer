import logging
from collections.abc import Collection
from typing import Optional
import csv


class MovieCatalog:
    _instance = None

    def __init__(self):
        self.movie = []
        with open('data/movies.csv', 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:

                # Skip blank line
                if not row:
                    continue

                # Skip comment line
                if row[0].startswith('#'):
                    continue

                # Check if invalid
                if len(row) != 4:
                    error_line = ','.join([x for x in row])
                    logging.log(logging.ERROR, f"Unrecognized format "
                                               f"{error_line}")
                    continue

                title = row[1]
                year = int(row[2])
                genre = row[3].split('|')

                this_movie = Movie(title, year, genre)
                self.movie.append(this_movie)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    def get_movie(self, title: str, year: Optional[int] = None):

        for movie in self.movie:
            if movie.title == title and (year is None or movie.year == year):
                return movie
        return None


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


if __name__ == "__main__":
    a = MovieCatalog()