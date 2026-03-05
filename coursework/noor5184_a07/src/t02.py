"""
-------------------------------------------------------
Sorted_List required-methods test driver (t02)
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:      169105184
Email:   Noor5184@mylaurier.ca
__updated__ = "2025-11-08"
-------------------------------------------------------
"""
from Sorted_List_linked import Sorted_List
from Movie import Movie


def sample_movies():
    """
    -------------------------------------------------------
    Builds a small set of Movie instances for testing.
    Use:
    -------------------------------------------------------
    Returns:
        data - tuple of Movie objects (tuple)
    ------------------------------------------------------
    """
    data = (
        Movie("Aliens", 1986, "James Cameron", 8.3, [0, 6]),
        Movie("The Godfather", 1972, "Francis Ford Coppola", 9.2, [2, 10]),
        Movie("The Godfather Part II", 1974, "Francis Ford Coppola", 9.0, [2, 10]),
        Movie("Arrival", 2016, "Denis Villeneuve", 7.9, [0, 2]),
        Movie("Gladiator", 2000, "Ridley Scott", 8.5, [6, 7, 9]),
        Movie("Alien", 1979, "Ridley Scott", 8.5, [0, 8]),
        Movie("Alien", 1979, "Ridley Scott", 8.5, [0, 8]),
        Movie("Zodiac", 2007, "David Fincher", 7.7, [10, 2]),
    )
    return data


def print_list(title, sl):
    """
    -------------------------------------------------------
    Prints a Sorted_List of Movies.
    Use:
    -------------------------------------------------------
    Parameters:
        title - header (str)
        sl - list to print (Sorted_List)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"\n{title}")
    print(f"count={len([*sl])}")
    for v in sl:
        print(v)
    return


def build_sorted(values):
    """
    -------------------------------------------------------
    Inserts values into a new Sorted_List.
    Use:
    -------------------------------------------------------
    Parameters:
        values - iterable of Movie (iterable)
    Returns:
        sl - populated Sorted_List (Sorted_List)
    ------------------------------------------------------
    """
    sl = Sorted_List()
    for v in values:
        sl.insert(v)
    return sl


def test_insert_get_contains_index_find():
    """
    -------------------------------------------------------
    Tests insert, __getitem__, __contains__, index, find.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g, h = sample_movies()
    sl = Sorted_List()
    for m in (d, b, a, e, c, h, f):
        sl.insert(m)
    print_list("After sorted insertions", sl)
    print("getitem [0]:", sl[0])
    print("getitem [-1]:", sl[-1])
    probe = Movie("Alien", 1979, "X", None, None)
    print("contains 'Alien' 1979:", probe in sl)
    print("index of 'Alien' 1979:", sl.index(probe))
    print("find 'Godfather':", sl.find(Movie("The Godfather", 1972, "", None, None)))
    return


def test_remove_and_remove_front():
    """
    -------------------------------------------------------
    Tests remove and remove_front.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g, h = sample_movies()
    sl = build_sorted((f, g, a, b, c, d))
    print_list("Original for removal", sl)
    first = sl.remove_front()
    print("\nremove_front returned:", first)
    print_list("After remove_front", sl)
    rem = sl.remove(Movie("The Godfather", 1972, "", None, None))
    print("\nremove key returned:", rem)
    print_list("After remove(key)", sl)
    missing = sl.remove(Movie("Nonexistent", 2000, "", None, None))
    print("\nremove missing returned:", missing)
    return


def test_min_max_peek():
    """
    -------------------------------------------------------
    Tests min, max, and peek.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g, h = sample_movies()
    sl = build_sorted((d, e, a, b, c, h))
    print_list("For min/max/peek", sl)
    print("min:", sl.min())
    print("max:", sl.max())
    print("peek:", sl.peek())
    return


def test_count_and_clean():
    """
    -------------------------------------------------------
    Tests count and clean.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g, h = sample_movies()
    sl = build_sorted((a, b, a, c, a, d, b, e, c, f, g))
    print_list("Before clean (with duplicates)", sl)
    key = Movie("Alien", 1979, "", None, None)
    print("count of 'Alien' 1979:", sl.count(key))
    sl.clean()
    print_list("After clean (first occurrences preserved)", sl)
    print("count of 'Alien' 1979 after clean:", sl.count(key))
    return


def test_union_and_intersection_and_eq():
    """
    -------------------------------------------------------
    Tests union, intersection, and equality.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g, h = sample_movies()
    s1 = build_sorted((a, c, e, g))
    s2 = build_sorted((b, c, d, f, g))
    u = Sorted_List()
    u.union(s1, s2)
    print_list("union(s1,s2)", u)
    i = Sorted_List()
    i.intersection(s1, s2)
    print_list("intersection(s1,s2)", i)
    s3 = build_sorted((a, c, e, g))
    print("s1 == s3:", s1 == s3)
    print("s1 == s2:", s1 == s2)
    return


def main():
    """
    -------------------------------------------------------
    Runs all required Sorted_List tests.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    print("SORTED_LIST REQUIRED METHODS TESTS")
    print("----------------------------------")
    test_insert_get_contains_index_find()
    print("\n== remove / remove_front ==")
    test_remove_and_remove_front()
    print("\n== min / max / peek ==")
    test_min_max_peek()
    print("\n== count / clean ==")
    test_count_and_clean()
    print("\n== union / intersection / __eq__ ==")
    test_union_and_intersection_and_eq()
    return


if __name__ == "__main__":
    main()
