# Project Full-Data
Full and comprehensive object oriented back end for core data management needs focused on building the core primitives used in real systems like indexing, fast lookup, and ordered retrieval, from scratch. Developed an in-memory and highly adaptable object indexing and management backend in Python. Designed reusable ADTs and algorithms, including but not limited to, hash based lookup and management, BST organization, doubly linked list traversal, and multiple sorting strategies to enable fast object search, insert/remove, and sorted views. Emphasized modular OOP architecture and test driven validation with emphasis on design and user experience, and a focus on performance oriented operations and optimization metrics.

This repository is a comprehensive Python implementation of core data structures and algorithms organized around clean ADT-style interfaces. It includes:

- A shared data-structures backend (“library”) that contains the actual implementations.
- Full lab (`lXX`) and assignment (`aXX`) modules that include many runnable tester scripts (`t01.py`, `t02.py`, …) demonstrating and validating features.
- A runner utility that recreates the original Eclipse/PyDev “referenced project” behavior so everything runs correctly on any machine after cloning.

---

## What’s Implemented (High Level)

The shared backend (the main “engine”) includes implementations and algorithms across:

- Linear ADTs: stacks, queues, circular queues, deques, priority queues  
- Lists: array-based lists, linked lists, sorted lists  
- Trees: linked Binary Search Tree (BST)  
- Hashing: hash-set variants (multiple strategies)  
- Sorting: classic sorting algorithms applied to arrays and linked structures  
- Object handling: example domain objects used for ordering/searching (e.g., Movie/Word/Number)

---

## Repository Layout

- `noor5184_data_structures/`  
  Shared backend “library” used throughout labs/assignments.  
  Key code lives in: `noor5184_data_structures/src/`

- `coursework/`  
  Full lab (`noor5184_lXX`) and assignment (`noor5184_aXX`) modules.  
  Each module contains runnable tester scripts (commonly `t01.py`, `t02.py`, etc.), usually inside a `src/` folder.

- `runners/`  
  Runner utilities that make testers runnable from the repo root on a standard Python installation.

---

## How To Run (Full Project: Any Lab/Assignment Tester)

### Why a runner is needed
In the original Eclipse/PyDev setup, `noor5184_data_structures/src` was configured as a referenced project, which made imports like:

`from Stack_array import Stack`

work automatically inside lab/assignment code.

A normal Python environment does not include that path by default. To make the project runnable anywhere after cloning, use the provided runner which injects the correct `PYTHONPATH` and runs testers with the correct working directory.

### Run any tester with `run_tester.py`
From the repository root:

**Windows**
    python runners\run_tester.py <relative-path-to-tester>

**macOS/Linux**
    python runners/run_tester.py <relative-path-to-tester>

### Example command
**Windows**
    python runners\run_tester.py coursework\noor5184_a03\src\t05.py

**macOS/Linux**
    python runners/run_tester.py coursework/noor5184_a03/src/t05.py

### How to find testers
Most testers are located under `coursework/` inside lab/assignment folders, usually in a `src/` subfolder.

Common patterns:
- `coursework/noor5184_aXX/src/t01.py`
- `coursework/noor5184_aXX/src/t02.py`
- `coursework/noor5184_lXX/src/t01.py`

To list testers in a given module:

**Windows**
    dir coursework\noor5184_a03\src

**macOS/Linux**
    ls coursework/noor5184_a03/src

### Notes about output / behavior
- Some testers print results to the console.
- Some testers validate correctness without printing; an exit code of `0` indicates success.
- `run_tester.py` runs the tester with the tester’s own folder as the working directory so relative file access (if any) behaves as expected.

---

## Curated Demos (Quick Portfolio Tour)

If you want a quick “best-of” tour without searching through the folder structure, use the curated demo runner (if included in this repo):

**Windows**
    python runners\run_demo.py list
    python runners\run_demo.py <demo-name>

**macOS/Linux**
    python runners/run_demo.py list
    python runners/run_demo.py <demo-name>

The curated runner maps short demo names (e.g., `postfix`, `maze`, etc.) to specific tester scripts under `coursework/` and runs them through the same environment setup as `run_tester.py`.

---

## Attribution / Provenance (Important)

This repository includes course-based lab/assignment structure and may include starter templates/interfaces provided by the CP164 course. Implementations and modifications are mine where indicated, and the project is presented here as a portfolio demonstration of data structures, algorithms, and ADT-based design in Python.re and may include starter templates/interfaces provided by the CP164 course. Implementations and modifications are mine where indicated, and the project is presented here as a portfolio demonstration of data structures, algorithms, and ADT-based design in Python.
