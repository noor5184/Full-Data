"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-10-04"
-------------------------------------------------------
"""
# Imports

# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


class Movie:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    MIN_RATING = 0
    MAX_RATING = 10
    FIRST_YEAR = 1888
    GENRES = ("science fiction", "fantasy", "drama",
              "romance", "comedy", "zombie", "action",
              "historical", "horror", "war", "mystery")
    GENRE_CODES = range(len(GENRES))

    @staticmethod
    def genres():
        """
        -------------------------------------------------------
        Creates a string of Movie genres in the format:
         0 science fiction
         1 fantasy
         ...
        Use: s = Movie.genres()
        -------------------------------------------------------
        Returns:
            string - A numbered string of Movie.genres.
        -------------------------------------------------------
        """
        string = "\n".join(f"{i} {name}" for i, name in enumerate(Movie.GENRES))
        return string

    def __init__(self, title, year, director, rating, genres):
        """
        -------------------------------------------------------
        Initializes a Movie object.
        Use: movie = Movie(title, year, director, rating, genres)
        -------------------------------------------------------
        Parameters:
            title - movie title (str)
            year - year of release (int)
            director - name of director (str)
            rating - rating of 1 - 10 from IMDB (float)
            genres - numbers representing movie genres_list (list of int)
        Returns:
            A new Movie object (Movie)
        -------------------------------------------------------
        """
        assert year >= Movie.FIRST_YEAR, "Movie year must be >= {}".format(
            Movie.FIRST_YEAR)
        assert rating is None or Movie.MIN_RATING <= rating <= Movie.MAX_RATING, \
            "Movie ratings must be between {} and {}".format(
                Movie.MIN_RATING, Movie.MAX_RATING)
        assert genres is None or genres == [] or min(genres) in Movie.GENRE_CODES, "Invalid genre code {}".format(
            min(genres))
        assert genres is None or genres == [] or max(genres) in Movie.GENRE_CODES, "Invalid genre code {}".format(
            max(genres))

        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genres = genres

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of movie data.
        Use: print(movie)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of movie (str)
        -------------------------------------------------------
        """
        genres_list = self.genres_string()
        rating_str = "None" if self.rating is None else f"{self.rating}"
        genres_str = "" if genres_list == "" else genres_list
        string = f"{self.title} ({self.year}), dir. {self.director}, rating: {rating_str}, genres: {genres_str}"
        return string

    def __eq__(self, other):
        """
        -------------------------------------------------------
        Compares this movie against another movie for equality.
        Use: movie == other
        -------------------------------------------------------
        Parameters:
            other - other movie to compare to (Movie)
        Returns:
            result - True if title and year match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.title.lower(), self.year) == \
            (other.title.lower(), other.year)
        return result

    def __lt__(self, other):
        """
        -------------------------------------------------------
        Determines if this movie comes before another movie.
        Use: movie < other
        -------------------------------------------------------
        Parameters:
            other - movie to compare to (Movie)
        Returns:
            result - True if movie precedes other, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.title.lower(), self.year) < \
            (other.title.lower(), other.year)
        return result

    def __le__(self, other):
        """
        -------------------------------------------------------
        Determines if this movie precedes or is or equal to another movie.
        Use: movie <= other
        -------------------------------------------------------
        Parameters:
            other - movie to compare to (Movie)
        Returns:
            result - True if this movie precedes or is equal to other,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        result = self < other or self == other
        return result

    def genres_string(self):
        """
        -------------------------------------------------------
        Returns comma delimited string of genres based upon the
        current movie object's integer genres list.
        e.g.: [0, 2] returns "science fiction, drama"
        Use: string = movie.genres_string()
        -------------------------------------------------------
        Returns:
            string - string of genres (str)
        -------------------------------------------------------
        """
        if self.genres is None or self.genres == []:
            return ""
        string = ", ".join(Movie.GENRES[i] for i in self.genres)
        return string

    def genres_list_string(self):
        """
        -------------------------------------------------------
        Returns comma delimited string of genre indexes based upon the
        current movie object's integer genres list.
        e.g.: [0, 2] returns "0,2"
        Use: string = movie.genres_list_string()
        -------------------------------------------------------
        Returns:
            string - string of genre indexes (str)
        -------------------------------------------------------
        """
        if self.genres is None or self.genres == []:
            return ""
        string = ",".join(str(i) for i in self.genres)
        return string

    def write(self, fv):
        """
        -------------------------------------------------------
        Writes a single line of movie data to an open file fv
        in the format
              title|year|director|rating|code
        Use: movie.write(fv)
        -------------------------------------------------------
        Parameters:
            fv - an already open file of movie data (file)
        Returns:
            None
        -------------------------------------------------------
        """
        fv.write(f"{self.title}|{self.year}|{self.director}|{self.rating}|{self.genres_list_string()}\n")
        return