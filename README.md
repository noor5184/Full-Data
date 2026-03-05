# Project Full-Data
Full and comprehensive object oriented back end for core data management needs focused on building the core primitives used in real systems like indexing, fast lookup, and ordered retrieval, from scratch. Developed an in-memory and highly adaptable object indexing and management backend in Python. Designed reusable ADTs and algorithms, including but not limited to, hash based lookup and management, BST organization, doubly linked list traversal, and multiple sorting strategies to enable fast object search, insert/remove, and sorted views. Emphasized modular OOP architecture and test driven validation with emphasis on design and user experience, and a focus on performance oriented operations and optimization metrics.


## What’s Implemented (High Level)

The shared backend contains implementations and algorithms across:
- Linear ADTs: stacks, queues, circular queues, deques, priority queues
- Lists: array-based lists, linked lists, sorted lists
- Trees: linked Binary Search Tree (BST)
- Hashing: hash-set variants (multiple strategies)
- Sorting: classic sorting algorithms applied to arrays and linked structures
- Object handling: example domain objects used for ordering/searching (e.g., Movie/Word/Number)

## Repository Layout

- `noor5184_data_structures/`
  - Shared backend “library” used throughout labs/assignments
  - Key code lives in: `noor5184_data_structures/src/`
- `coursework/`
  - Full lab (`noor5184_lXX`) and assignment (`noor5184_aXX`) modules
  - Contains runnable tester scripts (usually named `t01.py`, `t02.py`, etc.)
- `runners/`
  - Utilities that make the project runnable from the repo root in a standard Python environment

## How To Run (Recommended)

### Why a runner is needed
In the original Eclipse/PyDev course setup, `noor5184_data_structures/src` was configured as a referenced project, which made imports like:

`from Stack_array import Stack`

work automatically. A normal Python environment does not include that path by default.

This repo includes a runner that injects the correct path automatically so everything runs on any machine after cloning.

### Run any lab/assignment tester
From the repository root:

Windows:
    python runners\run_tester.py <relative-path-to-tester>

macOS/Linux:
    python runners/run_tester.py <relative-path-to-tester>

Example (postfix evaluator tester):
Windows:
    python runners\run_tester.py coursework\noor5184_a03\src\t05.py

macOS/Linux:
    python runners/run_tester.py coursework/noor5184_a03/src/t05.py

### Find available testers
Most testers live inside lab/assignment folders under `coursework/`, often in a `src/` subfolder.

Examples:
- coursework/noor5184_a03/src/t01.py
- coursework/noor5184_a03/src/t05.py
- coursework/noor5184_l07/src/t02.py

To list testers in a folder:

Windows:
    dir coursework\noor5184_a03\src

macOS/Linux:
    ls coursework/noor5184_a03/src

### Notes about output
- Some testers print results to the console.
- Some testers validate correctness without printing; exit code `0` indicates success.
- The runner executes each tester with the correct working directory so any relative file access behaves as expected.

## Curated Demos (Portfolio Tour)

If you want a quick “best-of” tour without searching through folders, use the curated demo runner (see `runners/run_demo.py` once added). It provides simple commands like:

    python runners\run_demo.py list
    python runners\run_demo.py postfix
    python runners\run_demo.py maze

## Attribution / Provenance (Important)
This repository contains course-based lab/assignment structure and may include starter templates/interfaces provided by the CP164 course. Implementations and modifications are mine where indicated, and the project is presented here as a portfolio demonstration of data structures, algorithms, and ADT-based design in Python.
