"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-09-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze

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



maze_simple = {
    "Start": ["A"],
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["X"],
    "F": []
}

maze_trivial = {"Start": ["X"]}

maze_no_exit = {"Start": ["A"], "A": ["A"]}

print("simple:", stack_maze(maze_simple))  
print("trivial:", stack_maze(maze_trivial))
print("no exit:", stack_maze(maze_no_exit))
