"""
-------------------------------------------------------
[Assignment 4, Task 5]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-10-04"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

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
    return None


def dump(label, q):

    arr = ["N" if x is None else x for x in q._values]
    print(f"{label}  _values={arr}  front={q._front}  rear={q._rear}  count={len(q)}  empty={q.is_empty()}  full={q.is_full()}")
    return None


def fill(q, items):
    """
    Inserts items into a circular queue in sequence.
    """
    for x in items:
        q.insert(x)
    return None


def main():

    q = Queue(7)
    print("== Basic inserts ==")
    fill(q, [1, 2, 7, 9])
    show("q      ", q)
    dump("state  ", q)

    print("\n== Peek and length ==")
    print("peek:", q.peek())
    print("len :", len(q))

    print("\n== Remove two, then wrap with three inserts ==")
    a = q.remove()
    b = q.remove()
    print("removed:", a, b)
    fill(q, [1, 2, 7])
    show("q      ", q)
    dump("state  ", q)

    print("\n== Fill to capacity and test is_full ==")
    fill(q, [9])
    show("q      ", q)
    dump("state  ", q)

    print("\n== Drain queue completely and test is_empty ==")
    drained = []
    while not q.is_empty():
        drained.append(q.remove())
    print("drained:", drained)
    dump("state  ", q)

    print("\n== Equality with different internal layouts ==")
    qa = Queue(7)
    fill(qa, [1, 2, 7, 9])

    qb = Queue(7)
    fill(qb, [7, 9, 1, 2])
    x = qb.remove()
    qb.insert(x)
    y = qb.remove()
    qb.insert(y)

    show("qa     ", qa)
    dump("qa int ", qa)
    show("qb     ", qb)
    dump("qb int ", qb)
    print("qa == qb ?", qa == qb)

    return None


if __name__ == "__main__":
    main()
