"""
-------------------------------------------------------
[Run curated CP164 tester from the repo root while emulating the IDE "referenced project" 
path. Usage (from repo root):python runners/run_tester.py]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-09-11"
-------------------------------------------------------
"""
# Imports
from __future__ import annotations

import sys

from run_tester import run_tester
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


"""
Curated demos (portfolio entry points).

Use:
    python runners\\run_demo.py list
    python runners\\run_demo.py <demo>
    python runners\\run_demo.py all
"""



DEMO_MAP = {
    "postfix": (
        "coursework/noor5184_a03/src/t05.py",
        "Postfix evaluator (stack application)",
    ),
    "maze": (
        "coursework/noor5184_a03/src/t06.py",
        "Maze solver (DFS using a stack)",
    ),
    "reroute": (
        "coursework/noor5184_a03/src/t07.py",
        "Rail-yard reroute simulation (stack operations)",
    ),
    "list_array": (
        "coursework/noor5184_l04/src/t01.py",
        "List ADT demo (array-backed): append/insert/remove/find/min/max/get/set",
    ),
    
    "sorts_array": (
        "coursework/noor5184_l10/src/test_Sorts_array.py",
        "Sorting algorithms on arrays (comparison of classic sorts)",
    ),
    "sorts_linked": (
        "coursework/noor5184_l10/src/test_Sorts_List_linked.py",
        "Sorting algorithms on linked lists (linked-structure sorting)",
    ),
    "l10_t01": (
        "coursework/noor5184_l10/src/t01.py",
        "Lab 10 tester t01 (sorting / verification)",
    ),
    "l10_t02": (
        "coursework/noor5184_l10/src/t02.py",
        "Lab 10 tester t02 (linked sorting / verification)",
    ),
    
    
    "pq_split_key_func": (
        "coursework/noor5184_a04/src/t03.py",
        "Priority Queue partition by key (function): split into (> key) and (<= key), drains source",
    ),
    "pq_split_key_method": (
        "coursework/noor5184_a04/src/t04.py",
        "Priority Queue split_key (method): OOP implementation of key-based partition + edge cases",
    ),
    "circular_queue_wrap": (
        "coursework/noor5184_a04/src/t05.py",
        "Circular Queue (ring buffer): wraparound insert/remove, full/empty invariants, equality across layouts",
    ),
    
    "list_movies": (
        "coursework/noor5184_a05/src/t01.py",
        "Array List ADT + Movie objects: comprehensive ops (combine/split/union/intersection) + edge cases",
    ),
    "sorted_list_movies": (
        "coursework/noor5184_a05/src/t02.py",
        "Sorted List (array) + Movie objects: ordered insert, split_key partitioning, duplicates/clean, queries",
    ),
    
    "list_linked_movies": (
        "coursework/noor5184_a07/src/t01.py",
        "Linked List ADT + Movie objects: core ops + split/clean/combine/union/intersection (duplicates & edge cases)",
    ),
    "sorted_linked_movies": (
        "coursework/noor5184_a07/src/t02.py",
        "Sorted Linked List + Movie objects: ordered insert, search/index/find, remove, clean/count, union/intersection",
    ),
    
    "hashset_array_buckets": (
        "coursework/noor5184_a09/src/t01.py",
        "Hash Set benchmark (array buckets): insert words from gibbon.txt, report total & worst-case comparisons",
    ),
    "hashset_sorted_buckets": (
        "coursework/noor5184_a09/src/t02.py",
        "Hash Set benchmark (sorted buckets): compare insertion comparisons vs array buckets",
    ),
    "hashset_bst_buckets": (
        "coursework/noor5184_a09/src/t03.py",
        "Hash Set benchmark (BST buckets): compare insertion comparisons vs list-based buckets",
    ),
    "bst_parent_counts": (
        "coursework/noor5184_a09/src/t04.py",
        "BST linked: inorder traversal, membership, node counts, parent lookup (iterative vs recursive)",
    ),
}


def _print_list() -> None:
    for key, (_, label) in DEMO_MAP.items():
        print(f"{key:12}  {label}")
    return


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] in {"-h", "--help"}:
        print(__doc__.strip())
        return 0

    cmd = argv[1].strip().lower()

    if cmd == "list":
        _print_list()
        return 0

    if cmd == "all":
        rc = 0
        for key in DEMO_MAP:
            rel_path, label = DEMO_MAP[key]
            print(f"\n=== Demo: {key} — {label} ===")
            code = run_tester(rel_path)
            if code != 0 and rc == 0:
                rc = code
        return rc

    if cmd not in DEMO_MAP:
        print(f"Unknown demo: {cmd}")
        print("Try: python runners\\run_demo.py list")
        return 2

    rel_path, label = DEMO_MAP[cmd]
    print(f"=== Demo: {cmd} — {label} ===")
    return run_tester(rel_path)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))