"""
-------------------------------------------------------
[Assignment 4, Task 1]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-10-04"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from functions import queue_combine
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





def show(label, q):

    print(label, end="  ")
    first = True
    for v in q:
        if not first:
            print(", ", end="")
        print(v, end="")
        first = False
    print()


def fill(q, items):

    for x in items:
        q.insert(x)


def main():

    s1 = Queue()
    s2 = Queue()
    fill(s1, [5, 8, 12, 8])
    fill(s2, [7, 9, 14])

    show("source1", s1)
    show("source2", s2)

    tgt = queue_combine(s1, s2)

    show("target ", tgt)
    show("source1 (empty check)", s1)
    show("source2 (empty check)", s2)


if __name__ == "__main__":
    main()