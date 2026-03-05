"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-10-11"
-------------------------------------------------------
"""
# Imports
from List_array import List
from Movie import Movie
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



def mk(title, year, director="Dir", rating=7.0, genres=None):
    if genres is None:
        genres = []
    m = Movie(title, year, director, rating, genres)
    return m

def header(text):
    print("========================================")
    print(text)
    print("========================================")

def as_list(L):
    items = []
    n = L._count if hasattr(L, "_count") else len(L)
    i = 0
    while i < n:
        items.append(L[i])
        i += 1
    return items

def show_state(name, L):
    n = L._count if hasattr(L, "_count") else len(L)
    print(f"{name} count={n} -> {[str(x) for x in as_list(L)]}")

def build_sample_movies():
    return [
        mk("Alpha", 2001),
        mk("Bravo", 2002),
        mk("Charlie", 2003),
        mk("Delta", 2004),
        mk("Echo", 2005),
    ]

def test_basic_mutators():
    header("Append / Prepend / __getitem__ / remove_front / remove_many / clean")
    L = List()
    show_state("Start (empty)", L)

    a, b, c, d, e = build_sample_movies()

    L.append(a)
    L.append(b)
    L.append(c)
    show_state("After append a,b,c", L)

    L.prepend(d)
    show_state("After prepend d", L)

    try:
        v = L[1]
        print(f"__getitem__(1) -> {v}")
    except Exception as ex:
        print(f"__getitem__ raised: {ex}")

    L.remove_front()
    show_state("After remove_front", L)

    L.append(b)
    L.append(a)
    show_state("After appending duplicates", L)

    L.remove_many(b)
    show_state("After remove_many(b)", L)

    L.append(a)
    L.append(a)
    L.append(c)
    show_state("Before clean (dups added)", L)

    L.clean()
    show_state("After clean (first occurrences preserved)", L)

def test_equality():
    header("__eq__")
    A = List()
    B = List()
    x, y, z = build_sample_movies()[:3]
    A.append(x); A.append(y); A.append(z)
    B.append(x); B.append(y); B.append(z)
    print(f"A == B -> {A == B}")
    B.remove_front()
    print(f"A == B after B.remove_front() -> {A == B}")

def test_combine():
    header("combine(source1, source2)")
    S1 = List()
    S2 = List()
    t1, t2, t3, t4, t5 = build_sample_movies()
    S1.append(t1); S1.append(t3); S1.append(t5)
    S2.append(t2); S2.append(t4)
    T = List()
    show_state("S1 before", S1)
    show_state("S2 before", S2)
    T.combine(S1, S2)
    show_state("Target after combine", T)
    show_state("S1 after (empty)", S1)
    show_state("S2 after (empty)", S2)

def test_split_and_split_alt():
    header("split() and split_alt()")
    L = List()
    m1, m2, m3, m4, m5 = build_sample_movies()
    L.append(m1); L.append(m2); L.append(m3); L.append(m4); L.append(m5)
    show_state("Source before split", L)
    A, B = L.split()
    show_state("Split target1", A)
    show_state("Split target2", B)
    show_state("Source after split (empty)", L)

    L2 = List()
    n1, n2, n3, n4 = build_sample_movies()[:4]
    L2.append(n1); L2.append(n2); L2.append(n3); L2.append(n4)
    show_state("Source before split_alt", L2)
    C, D = L2.split_alt()
    show_state("split_alt target1", C)
    show_state("split_alt target2", D)
    show_state("Source after split_alt (empty)", L2)

def test_union_and_intersection():
    header("union(source1, source2) and intersection(source1, source2)")
    S1 = List()
    S2 = List()
    a, b, c, d, e = build_sample_movies()
    S1.append(a); S1.append(b); S1.append(c); S1.append(b)
    S2.append(c); S2.append(d); S2.append(e); S2.append(a)
    show_state("S1", S1)
    show_state("S2", S2)

    U = List()
    U.union(S1, S2)
    show_state("Union(S1,S2)", U)

    I = List()
    I.intersection(S1, S2)
    show_state("Intersection(S1,S2)", I)

def test_empty_cases():
    header("Empty-list edge cases")
    E = List()
    show_state("Empty start", E)
    try:
        E.remove_front()
    except Exception as ex:
        print(f"remove_front on empty raised: {ex}")
    F = List(); G = List(); H = List()
    H.union(F, G)
    show_state("Union of two empties", H)
    I = List(); J = List(); K = List()
    K.intersection(I, J)
    show_state("Intersection of two empties", K)
    L0 = List()
    A, B = L0.split()
    show_state("Split empty target1", A)
    show_state("Split empty target2", B)
    L1 = List()
    C, D = L1.split_alt()
    show_state("Split_alt empty target1", C)
    show_state("Split_alt empty target2", D)

def main():
    header("List_array — Movie ADT Comprehensive Test")
    test_basic_mutators()
    test_equality()
    test_combine()
    test_split_and_split_alt()
    test_union_and_intersection()
    test_empty_cases()
    print("All tests completed.")

if __name__ == "__main__":
    main()
