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
from Sorted_List_array import Sorted_List
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
    


from Movie import Movie


# -----------------------------------------------------------------------------
# Small helpers
# -----------------------------------------------------------------------------
def mk(title, year, director="Dir", rating=7.0, genres=None):
    if genres is None:
        genres = []
    return Movie(title, year, director, rating, genres)

def header(text):
    print("========================================")
    print(text)
    print("========================================")

def as_list(L):
    """Use the ADT to read elements so we also exercise __getitem__."""
    out = []
    i = 0
    while i < L._count:
        out.append(L[i])
        i += 1
    return out

def show_state(name, L):
    print(f"{name} count={L._count} -> {[str(x) for x in as_list(L)]}")

def seed_sorted_movies():
    
    return [
        mk("Alpha",   2001),
        mk("Bravo",   2002),
        mk("Charlie", 2003),
        mk("Delta",   2004),
        mk("Echo",    2005),
    ]
    
    



def as_list(L):
    """
    Build a Python list from the ADT by indexing until it fails.
    This avoids touching internals like _count/_values.
    """
    out = []
    i = 0
    while True:
        try:
            out.append(L[i])   # exercises __getitem__
            i += 1
        except Exception:
            break
    return out

def show_state(name, L):
    """
    Print a labeled snapshot of the list using only public behavior.
    """
    items = as_list(L)
    try:
        n = len(L)             # if __len__ is implemented
    except Exception:
        n = len(items)
    print(f"{name} count={n} -> {[str(x) for x in items]}")
  
    



# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------
def test_core_create_and_order():
    header("create + automatic sorting via insert")
    L = Sorted_List()
    a, b, c, d, e = seed_sorted_movies()
    
    L.insert(c); L.insert(a); L.insert(e); L.insert(b); L.insert(d)
    show_state("After inserts (expect A..E order)", L)

def test_contains_eq_getitem():
    header("__contains__, __eq__, __getitem__")
    L1 = Sorted_List()
    L2 = Sorted_List()
    a, b, c, d, e = seed_sorted_movies()
    for x in [e, c, a, d, b]:
        L1.insert(x)
        L2.insert(x)
    print(f"Contains 'Charlie' -> {c in as_list(L1)} (list view only)")
    print(f"L1 == L2 -> {L1 == L2}")
    print(f"L1[2] -> {L1[2]}")

def test_clean_and_count_find_index_min_max_peek():
    header("clean, count, find, index, min, max, peek")
    L = Sorted_List()
    a, b, c, d, e = seed_sorted_movies()
    
    for x in [a, b, b, c, c, c, d, e, e]:
        L.insert(x)
    show_state("Start (with duplicates)", L)

    print(f"count(Alpha)   -> {L.count(a)}")
    print(f"count(Bravo)   -> {L.count(b)}")
    print(f"count(Charlie) -> {L.count(c)}")
    print(f"count(Echo)    -> {L.count(e)}")

    print(f"find(Delta) -> {L.find(d)}")
    print(f"index(Charlie) -> {L.index(c)}")

    print(f"min()  -> {L.min()}")
    print(f"max()  -> {L.max()}")
    print(f"peek() -> {L.peek()}")

    L.clean()
    show_state("After clean (duplicates removed)", L)

def test_remove_remove_front_remove_many():
    header("remove, remove_front, remove_many")
    L = Sorted_List()
    a, b, c, d, e = seed_sorted_movies()
    for x in [a, b, b, c, d, d, d, e]:
        L.insert(x)
    show_state("Start", L)

    v = L.remove(b)
    print(f"remove(Bravo) -> {v}")
    show_state("After remove(Bravo) (first occurrence only)", L)

    v = L.remove_front()
    print(f"remove_front() -> {v}")
    show_state("After remove_front()", L)

    L.remove_many(d)
    show_state("After remove_many(Delta) (all Deltas gone)", L)

def test_split_and_split_alt():
    header("split() and split_alt()")
    L = Sorted_List()
    a, b, c, d, e = seed_sorted_movies()
    for x in [a, b, c, d, e]:
        L.insert(x)
    show_state("Before split", L)
    A, B = L.split()
    show_state("split target1 (>= half)", A)
    show_state("split target2 (<= half)", B)
    show_state("Source after split (empty)", L)

    L2 = Sorted_List()
    for x in [a, b, c, d, e]:
        L2.insert(x)
    show_state("Before split_alt", L2)
    C, D = L2.split_alt()
    show_state("split_alt target1 (even indexes)", C)
    show_state("split_alt target2 (odd indexes)", D)
    show_state("Source after split_alt (empty)", L2)

def test_split_key_union_intersection():
    header("split_key(key), union, intersection")
    a, b, c, d, e = seed_sorted_movies()

    
    L = Sorted_List()
    for x in [a, b, c, d, e]:
        L.insert(x)
    show_state("Before split_key(Charlie)", L)
    T1, T2 = L.split_key(c)  # < c  |  >= c
    show_state("split_key target1 (< Charlie)", T1)
    show_state("split_key target2 (>= Charlie)", T2)
    show_state("Source after split_key (empty)", L)

    
    S1 = Sorted_List(); S2 = Sorted_List(); U = Sorted_List()
    for x in [a, c, e, c]:
        S1.insert(x)
    for x in [b, c, d, e]:
        S2.insert(x)
    show_state("S1 (for union)", S1)
    show_state("S2 (for union)", S2)
    U.union(S1, S2)
    show_state("Union(S1,S2)", U)
    show_state("S1 after union (spec-dependent)", S1)
    show_state("S2 after union (spec-dependent)", S2)

    
    I = Sorted_List()
    I.intersection(S1, S2)
    show_state("Intersection(S1,S2)", I)

def test_empty_edge_cases():
    header("empty-list edge cases")
    L = Sorted_List()
    show_state("Empty start", L)

    
    print(f"(Alpha in empty) -> {mk('Alpha', 2001) in as_list(L)} (list view only)")

    
    try:
        print("peek() -> ", L.peek())
    except Exception as ex:
        print(f"peek raised: {ex}")
    try:
        print("min() -> ", L.min())
    except Exception as ex:
        print(f"min raised: {ex}")
    try:
        print("max() -> ", L.max())
    except Exception as ex:
        print(f"max raised: {ex}")

    print("find(Alpha) on empty -> ", L.find(mk("Alpha", 2001)))
    print("index(Alpha) on empty -> ", L.index(mk("Alpha", 2001)))
    print("count(Alpha) on empty -> ", L.count(mk("Alpha", 2001)))

    
    A, B = L.split()
    show_state("Split empty target1", A)
    show_state("Split empty target2", B)

    C, D = L.split_alt()
    show_state("Split_alt empty target1", C)
    show_state("Split_alt empty target2", D)

    E1, E2 = L.split_key(mk("Bravo", 2002))
    show_state("Split_key(empty) target1", E1)
    show_state("Split_key(empty) target2", E2)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    header("Sorted_List_array — Movie ADT Comprehensive Test")
    test_core_create_and_order()
    test_contains_eq_getitem()
    test_clean_and_count_find_index_min_max_peek()
    test_remove_remove_front_remove_many()
    test_split_and_split_alt()
    test_split_key_union_intersection()
    test_empty_edge_cases()
    print("All tests completed.")

if __name__ == "__main__":
    main()
