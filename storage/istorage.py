from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    Representing interface for persistent storage implementations
    """

    @abstractmethod
    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.
        """
        pass

    @abstractmethod
    def add_movie(self, title: str, year: int, rating: float, poster: str):
        """
        Gets all your movies as an argument and saves them to the file.
        """
        pass

    @abstractmethod
    def delete_movie(self, title: str):
        """
        Adds a movie to the movie database.
        Loads the information from the file, adds the movie,
        and saves it. The function doesn't need to validate the input.
        """
        pass

    @abstractmethod
    def update_movie(self, title: str, rating: float):
        """
        Deletes a movie from the movie database.
        Loads the information from the JSON file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """
        pass

    @abstractmethod
    def is_movie_in_storage(self, title: str):
        """
        Returns True if movie was found in the storage, otherwise False.
        """
        pass
