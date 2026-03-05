# Project Full-Data
Full and comprehensive object oriented back end for core data management needs focused on building the core primitives used in real systems like indexing, fast lookup, and ordered retrieval, from scratch. Developed an in-memory and highly adaptable object indexing and management backend in Python. Designed reusable ADTs and algorithms, including but not limited to, hash based lookup and management, BST organization, doubly linked list traversal, and multiple sorting strategies to enable fast object search, insert/remove, and sorted views. Emphasized modular OOP architecture and test driven validation with emphasis on design and user experience, and a focus on performance oriented operations and optimization metrics.

This repository is a comprehensive Python implementation of core data structures and algorithms organized around clean ADT-style interfaces. It includes:

- A shared data-structures backend (“library”) that contains the actual implementations.
- Full lab (`lXX`) and assignment (`aXX`) modules that include many runnable tester scripts (`t01.py`, `t02.py`, …) demonstrating and validating features.
- A runner utility that recreates the original Eclipse/PyDev “referenced project” behavior so everything runs correctly on any machine after cloning.

---

# Data Structures & Algorithms Backend (Python)

A portfolio repository showcasing a full suite of core data structures and algorithms implemented and exercised through extensive lab/assignment testers. The repo includes a shared “engine” library, the original coursework modules, and runner utilities so everything executes correctly on any machine after cloning (no Eclipse/PyDev referenced-project setup required).

## Quick Start (Recommended)

### Requirements

* Python 3.x installed (no external packages required)

### Run curated demos (fastest way to evaluate)

From the repository root (where you have saved the contents of file (ex. cd "%USERPROFILE%\OneDrive\Documents\ds-engine":

**Windows**

* `python runners\run_demo.py list`
* `python runners\run_demo.py postfix`
* `python runners\run_demo.py all`

**macOS/Linux**

* `python runners/run_demo.py list`
* `python runners/run_demo.py postfix`
* `python runners/run_demo.py all`

If you want to run a specific lab/assignment tester directly, use `run_tester.py` (see below).

---

## What’s Implemented

The shared backend contains implementations and algorithms across:

* **Linear ADTs:** stack, queue, circular queue, deque, priority queue
* **Lists:** array list, linked list, sorted list (array + linked)
* **Trees:** linked Binary Search Tree (BST)
* **Hashing:** hash-set variants with different bucket strategies
* **Sorting:** classic sorts across arrays, linked lists, and deques
* **Object modeling:** domain objects for ordering/searching (e.g., `Movie`, `Word`, `Number`)

---

## Repository Layout

* `noor5184_data_structures/`
  Shared backend “library” used throughout labs/assignments.
  Core code lives in: `noor5184_data_structures/src/`

* `coursework/`
  Full lab (`noor5184_lXX`) and assignment (`noor5184_aXX`) modules, including runnable tester scripts (`t01.py`, `t02.py`, …).

* `runners/`
  Runner utilities that make testers runnable from the repo root on a standard Python installation:

  * `run_tester.py` — run any tester by path
  * `run_demo.py` — run a curated set of “best-of” demos by name

---

## Running Any Tester (Full Project)

### Why a runner is needed

In the original Eclipse/PyDev course setup, `noor5184_data_structures/src` was configured as a referenced project, so imports like:

`from Stack_array import Stack`

worked automatically inside lab/assignment code.

A normal Python environment doesn’t include that path by default. `run_tester.py` recreates this behavior by injecting the correct `PYTHONPATH` and running testers with the correct working directory.

### Run any lab/assignment tester

From the repository root:

**Windows**

* `python runners\run_tester.py <relative-path-to-tester>`

**macOS/Linux**

* `python runners/run_tester.py <relative-path-to-tester>`

Example:

**Windows**

* `python runners\run_tester.py coursework\noor5184_a03\src\t05.py`

**macOS/Linux**

* `python runners/run_tester.py coursework/noor5184_a03/src/t05.py`

### Finding testers

Most testers are located under `coursework/` inside lab/assignment folders, often in a `src/` subfolder.

Examples:

* `coursework/noor5184_aXX/src/t01.py`
* `coursework/noor5184_lXX/src/t01.py`

List a module folder to see what’s available:

**Windows**

* `dir coursework\noor5184_a03\src`

**macOS/Linux**

* `ls coursework/noor5184_a03/src`

### Notes on output

* Some testers print results; others validate correctness quietly (exit code `0` indicates success).
* Some testers expect local data files (e.g., text corpora). The runner executes from the tester’s folder so relative file reads work as intended.

---

## Curated Demos (Portfolio Tour)

Use the curated runner to view the highest-signal demonstrations without searching through folders:

**Windows**

* `python runners\run_demo.py list`
* `python runners\run_demo.py <demo>`
* `python runners\run_demo.py all`

**macOS/Linux**

* `python runners/run_demo.py list`
* `python runners/run_demo.py <demo>`
* `python runners/run_demo.py all`

### Recommended demos to run

(These names correspond to keys in `runners/run_demo.py`.)

**Applied stacks**

* `postfix` — postfix expression evaluation using a stack
* `maze` — DFS maze solving using a stack
* `reroute` — stack-based rail-yard reroute simulation

**Queues / scheduling**

* `circular_queue_wrap` — circular queue (ring buffer) wraparound + full/empty invariants + equality
* `pq_split_key_func` — priority queue partition by key (standalone function)
* `pq_split_key_method` — priority queue partition by key (ADT method)

**Lists + object handling**

* `list_array` — array list ADT operations demo
* `list_movies` — array list + `Movie` objects (combine/split/union/intersection + edge cases)
* `sorted_list_movies` — sorted array list + `Movie` objects (ordered insert + split_key + duplicates/clean)
* `list_linked_movies` — linked list + `Movie` objects (core ops + transforms)
* `sorted_linked_movies` — sorted linked list + `Movie` objects (ordered insert + queries + union/intersection)

**Hashing + BST**

* `hashset_array_buckets` — hash set benchmark (array buckets) using word corpus; reports total/worst comparisons
* `hashset_sorted_buckets` — hash set benchmark (sorted buckets)
* `hashset_bst_buckets` — hash set benchmark (BST buckets)
* `bst_parent_counts` — BST traversal + node counts + parent lookup (iterative vs recursive)

**Sorting**

* `radix_array` — radix sort on arrays
* `radix_linked` — radix sort on linked list
* `gnome_array` — gnome sort on arrays + swap counter
* `gnome_deque` — gnome sort on deque + swap counter
* (Optional L10 demos can also be exposed here if included)

---

## Attribution / Provenance

This repository contains the original CP164 lab/assignment structure. Some modules began from course-provided skeletons/templates; implementations, extensions, and the lab/assignment solution work are mine where indicated. This repo is published as a portfolio demonstration of data structures, algorithms, ADT design, and correctness/performance testing in Python.
