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

class Stack:
    """
    -------------------------------------------------------
    Implementation of a Stack ADT using a Python list.
    -------------------------------------------------------
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Stack.
        Use: s = Stack()
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            result - True if stack is empty, False otherwise (bool)
        -------------------------------------------------------
        """
        result = len(self._values) == 0
        return result

    def push(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the top of the stack.
        Use: s.push(value)
        -------------------------------------------------------
        Parameters:
            value - data to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(value)

    def pop(self):
        """
        -------------------------------------------------------
        Removes and returns the top of stack.
        Use: value = s.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert not self.is_empty(), "Cannot pop from an empty stack"
        value = self._values.pop()
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of stack without
        removing it.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert not self.is_empty(), "Cannot peek at an empty stack"
        value = self._values[-1]
        return value
    
    
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source Stack into separate target Stacks with values
        alternating into the targets. At finish source Stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            result - a tuple (target1, target2) where target1 contains
                     alternating values from source and target2 contains
                     the other alternating values (tuple of Stack, Stack)
        -------------------------------------------------------
        """
        target1 = Stack()
        target2 = Stack()
        to_first = True
        while len(self._values) != 0:
            value = self._values.pop()
            if to_first:
                target1._values.append(value)
            else:
                target2._values.append(value)
            to_first = not to_first
        result = (target1, target2)
        return result
    
    
    
    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source Stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        temp = []
        while len(self._values) != 0:
            temp.append(self._values.pop())
        self._values = temp

