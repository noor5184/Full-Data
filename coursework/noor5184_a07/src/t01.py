"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:      169105184
Email:   Noor5184@mylaurier.ca
__updated__ = "2025-11-08"
-------------------------------------------------------
"""
from List_linked import List
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
    )
    return data


def print_list(title, lst):
    """
    -------------------------------------------------------
    Nicely prints a linked list of Movies.
    Use:
    -------------------------------------------------------
    Parameters:
        title - header to print (str)
        lst - linked list to print (List)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"\n{title}")
    print(f"count={len([*lst])}")
    for v in lst:
        print(v)
    return


def test_prepend_append_getitem():
    """
    -------------------------------------------------------
    Tests prepend, append, and __getitem__.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g = sample_movies()
    lst = List()
    lst.prepend(b)
    lst.prepend(a)
    lst.append(c)
    lst.append(d)
    print_list("After prepend/append", lst)
    print("getitem [0]:", lst[0])
    print("getitem [1]:", lst[1])
    print("getitem [-1]:", lst[-1])
    return


def test_eq():
    """
    -------------------------------------------------------
    Tests list equality (__eq__).
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g = sample_movies()
    l1 = List()
    l2 = List()
    for m in (a, b, c):
        l1.append(m)
    for m in (a, b, c):
        l2.append(m)
    print("l1 == l2:", l1 == l2)
    l2.append(d)
    print("l1 == l2 after extra append:", l1 == l2)
    return


def test_remove_front_and_remove_many():
    """
    -------------------------------------------------------
    Tests remove_front and remove_many.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g = sample_movies()
    lst = List()
    for m in (f, g, a, b, g, c, g, d):
        lst.append(m)
    print_list("Original with duplicates of 'Alien' 1979", lst)
    first = lst.remove_front()
    print("\nremove_front returned:", first)
    print_list("After remove_front", lst)
    key = Movie("Alien", 1979, "X", None, None)
    lst.remove_many(key)
    print_list("After remove_many(key='Alien' 1979)", lst)
    return


def test_split_and_split_alt():
    """
    -------------------------------------------------------
    Tests split and split_alt.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g = sample_movies()
    lst = List()
    for m in (a, b, c, d, e, f):
        lst.append(m)
    t1, t2 = lst.split()
    print_list("split: target1 (>=50%)", t1)
    print_list("split: target2 (<=50%)", t2)
    lst2 = List()
    for m in (a, b, c, d, e):
        lst2.append(m)
    u1, u2 = lst2.split_alt()
    print_list("split_alt: target1", u1)
    print_list("split_alt: target2", u2)
    return


def test_clean():
    """
    -------------------------------------------------------
    Tests clean.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g = sample_movies()
    lst = List()
    for m in (a, b, a, c, a, d, b, e, c, f, g):
        lst.append(m)
    print_list("Before clean", lst)
    lst.clean()
    print_list("After clean (first occurrences preserved)", lst)
    return


def test_combine_intersection_union():
    """
    -------------------------------------------------------
    Tests combine, intersection, and union.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    a, b, c, d, e, f, g = sample_movies()
    s1 = List()
    s2 = List()
    for m in (a, c, e, g):
        s1.append(m)
    for m in (b, c, d, f):
        s2.append(m)
    tgt = List()
    tgt.combine(s1, s2)
    print_list("combine target (interlaced, sources empty)", tgt)
    print_list("source1 after combine (should be empty)", s1)
    print_list("source2 after combine (should be empty)", s2)
    i1 = List()
    i1.intersection(tgt, tgt)
    print_list("intersection of target with itself", i1)
    u1 = List()
    s3 = List()
    s4 = List()
    for m in (a, b, a, d):
        s3.append(m)
    for m in (c, d, e, d):
        s4.append(m)
    u1.union(s3, s4)
    print_list("union of s3 and s4 (no repeats)", u1)
    return


def main():
    """
    -------------------------------------------------------
    Runs all required tests.
    Use:
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    print("REQUIRED METHODS TESTS")
    print("----------------------")
    test_prepend_append_getitem()
    print("\n== __eq__ ==")
    test_eq()
    print("\n== remove_front / remove_many ==")
    test_remove_front_and_remove_many()
    print("\n== split / split_alt ==")
    test_split_and_split_alt()
    print("\n== clean ==")
    test_clean()
    print("\n== combine / intersection / union ==")
    test_combine_intersection_union()
    return


if __name__ == "__main__":
    main()
