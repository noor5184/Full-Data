"""
-------------------------------------------------------
[Assignment 4, Task 4]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-10-04"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

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




def show(label, pq):

    print(label, end="  ")
    first = True
    for v in pq:
        if not first:
            print(", ", end="")
        print(v, end="")
        first = False
    print()
    return None


def fill(pq, items):

    for x in items:
        pq.insert(x)
    return None


def main():

    source = Priority_Queue()
    fill(source, [5, 12, 7, 3, 14, 9, 8])
    key = 8

    print("Before split_key:")
    show("source ", source)

    t1, t2 = source.split_key(key)

    print("\nAfter split_key with key =", key)
    show("target1 (> key)", t1)
    show("target2 (<= key)", t2)
    show("source (empty)", source)

    source2 = Priority_Queue()
    fill(source2, [1, 1, 1])
    key2 = 5
    print("\nEdge case: all <= key")
    show("source2 ", source2)
    a, b = source2.split_key(key2)
    show("t1 ", a)
    show("t2 ", b)
    show("source2 (empty)", source2)

    source3 = Priority_Queue()
    fill(source3, [10, 11, 12])
    key3 = 5
    print("\nEdge case: all > key")
    show("source3 ", source3)
    c, d = source3.split_key(key3)
    show("t1 ", c)
    show("t2 ", d)
    show("source3 (empty)", source3)
    return None


if __name__ == "__main__":
    main()
