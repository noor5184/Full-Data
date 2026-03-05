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
from List_array import List

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






def show(label, lst):

    print(label, end="  ")
    for i in range(lst._count):
        print(lst._values[i], end=" ")
    print(f"(count={lst._count})")
    return None


def main():

    print("===== TESTING List_array =====")
    source = List()

    # ---------- Append ----------
    print("\n-- append() --")
    for val in [10, 20, 30]:
        source.append(val)
    show("After appends", source)

    # ---------- Insert ----------
    print("\n-- insert() --")
    source.insert(0, 5)       # Prepend
    source.insert(2, 15)      # Insert in middle
    source.insert(10, 40)     # Append (out of range)
    show("After inserts", source)

    # ---------- Remove ----------
    print("\n-- remove() --")
    val = source.remove(15)
    print(f"Removed: {val}")
    val = source.remove(99)   # Nonexistent
    print(f"Removed (not found): {val}")
    show("After removes", source)

    # ---------- Count ----------
    print("\n-- count() --")
    source.append(20)
    source.append(20)
    show("Before count", source)
    print("Count of 20:", source.count(20))

    # ---------- Find & Index ----------
    print("\n-- find() & index() --")
    print("Find 30:", source.find(30))
    print("Find 100 (not found):", source.find(100))
    print("Index of 20:", source.index(20))
    print("Index of 50 (not found):", source.index(50))

    # ---------- Contains ----------
    print("\n-- __contains__ --")
    print("20 in list:", 20 in source)
    print("99 in list:", 99 in source)

    # ---------- Min & Max ----------
    print("\n-- min() and max() --")
    print("Min value:", source.min())
    print("Max value:", source.max())

    # ---------- __getitem__ & __setitem__ ----------
    print("\n-- __getitem__ & __setitem__ --")
    print("Item at index 2:", source[2])
    source[2] = 99
    print("After setting index 2 = 99")
    show("Current list", source)

    print("\n===== ALL TESTS COMPLETE =====")
    return None


if __name__ == "__main__":
    main()
