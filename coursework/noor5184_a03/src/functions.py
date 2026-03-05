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
from Stack_array import Stack
# Constants
OPERATORS = "+-*/"


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


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source Stack into two target Stacks by alternating pops.
    When finished, source is empty. Values are pushed alternately onto
    target1 and target2 in the order they are popped from source.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        result - a tuple (target1, target2), where:
                 target1 contains alternating values from source,
                 target2 contains the other alternating values
    -------------------------------------------------------
    """
    target1 = type(source)()
    target2 = type(source)()
    to_first = True
    while not source.is_empty():
        value = source.pop()
        if to_first:
            target1.push(value)
        else:
            target2.push(value)
        to_first = not to_first
    result = (target1, target2)
    return result



def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a Stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    temp1 = type(source)()
    temp2 = type(source)()
    while not source.is_empty():
        temp1.push(source.pop())
    while not temp1.is_empty():
        temp2.push(temp1.pop())
    while not temp2.is_empty():
        source.push(temp2.pop())







def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    for token in string.split():
        if len(token) == 1 and token in OPERATORS:
            right = s.pop()
            left = s.pop()
            if token == "+":
                s.push(left + right)
            elif token == "-":
                s.push(left - right)
            elif token == "*":
                s.push(left * right)
            else:
                s.push(left / right)
        else:
            s.push(float(token))
    answer = s.pop()
    return answer




def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using depth-first search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze; each key is a
               string like 'Start', 'A', 'B', ..., and 'X' is
               the exit (may appear as a neighbor but has no entry)
               (dict[str, list[str]])
    Returns:
        result - list of points from after 'Start' through 'X',
                 or None if no exit is reachable (list[str] or None)
    -------------------------------------------------------
    """
    s = Stack()
    path = ["Start"]
    visited = {"Start"}
    parent = {}
    for nb in sorted(maze.get("Start", [])):
        if nb not in visited and nb not in parent:
            parent[nb] = "Start"
            s.push(nb)
    result = None
    while not s.is_empty():
        node = s.pop()
        if node in visited:
            continue
        p = parent.get(node, None)
        while path[-1] != p:
            path.pop()
        path.append(node)
        if node == "X":
            result = path[1:]
            break
        visited.add(node)
        for nb in sorted(maze.get(node, [])):
            if nb not in visited and nb not in parent:
                parent[nb] = node
                s.push(nb)
    return result




def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to an operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto Stack,
                'X' means pop from Stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - string containing only 'S' and 'X' (str)
        values_in - a valid list (list of ?)
    Returns:
        result - if opstring is valid then a reordered copy of values_in,
                 otherwise None (list or None)
    -------------------------------------------------------
    """
    s = Stack()
    out = []
    i = 0
    valid = True
    for ch in opstring:
        if ch == "S":
            if i < len(values_in):
                s.push(values_in[i])
                i += 1
            else:
                valid = False
                break
        elif ch == "X":
            if not s.is_empty():
                out.append(s.pop())
            else:
                valid = False
                break
        else:
            valid = False
            break
    if valid and i == len(values_in) and s.is_empty() and len(out) == len(values_in):
        result = out
    else:
        result = None
    return result

