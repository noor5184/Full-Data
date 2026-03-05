"""
-------------------------------------------------------
Array version of the list ADT.
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-10-04"
-------------------------------------------------------
"""
from copy import deepcopy

DEFAULT_CAPACITY = 10000


class List:

    def __init__(self, capacity=DEFAULT_CAPACITY):
        """
        Initializes an empty array-based list.
        """
        assert capacity > 0, "List size must be > 0"
        self._values = [None] * capacity   # fixed-size array
        self._count = 0                    # number of used slots
        return

    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'
        value = self._values[i]

        return value

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        n = self._count

        return n

    def __setitem__(self, i, value):
        """
        -------------------------------------------------------
        The i-th element of list contains a copy of value. The existing
        value at i is overwritten.
        Use: source[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'
        self._values[i] = value

        return

    def __contains__(self, key):
        """
        -------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        i = self._linear_search(key)

        return i > -1

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Returns True if i is a valid index into the current list contents.
        Valid indexes are 0 .. _count - 1.
        -------------------------------------------------------
        """

        return isinstance(i, int) and 0 <= i < self._count

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the List.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of key in the List, -1 if key is not found (int)
        -------------------------------------------------------
        """
        i = 0
        index = -1
        while i < self._count and index == -1:
            if self._values[i] == key:
                index = i
            i += 1
        return index

    def _swap(self, i, j):
        """
        -------------------------------------------------------
        Swaps the position of two elements in the data list.
        The element originally at position i is now at position j,
        and visa versa.
        Private helper operations called only from within class.
        Use: self._swap(i, j)
        -------------------------------------------------------
        Parameters:
            i - index of one element to switch (int, 0 <= i < len(self._values))
            j - index of other element to switch (int, 0 <= j < len(self._values))
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index i'
        assert self._is_valid_index(j), 'Invalid index j'

        temp = self._values[i]
        self._values[i] = self._values[j]
        self._values[j] = temp

        return

    def append(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the end of the list.
        Use: source.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._count < len(self._values), "Cannot append to a full list."
        self._values[self._count] = value
        self._count += 1
        return

    def apply(self, func):
        """
        -------------------------------------------------------
        Applies an external function to every value in list.
        Use: source.apply(func)
        -------------------------------------------------------
        Parameters:
          func - a function that takes a single value as a parameter 
              and returns a value (function)
        Returns:
            None
        -------------------------------------------------------
        """
        i = 0
        while i < self._count:
            self._values[i] = func(self._values[i])
            i += 1

        return

    def clean(self):
        """
        -------------------------------------------------------
        The list contains one and only one of each value formerly present
        in the list. The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        i = 0
        while i < self._count:
            j = i + 1
            while j < self._count:
                if self._values[i] == self._values[j]:

                    for k in range(j, self._count - 1):
                        self._values[k] = self._values[k + 1]
                    self._count -= 1
                else:
                    j += 1
            i += 1
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._count == 0, "Target list must be empty."
    
        i = 0
        j = 0
        toggle = True 
    
        while i < source1._count or j < source2._count:
            if (toggle and i < source1._count) or j >= source2._count:
                self._values[self._count] = source1._values[i]
                i += 1
            elif (not toggle and j < source2._count) or i >= source1._count:
                self._values[self._count] = source2._values[j]
                j += 1
            self._count += 1
            toggle = not toggle
    
        
        source1._count = 0
        source2._count = 0
    
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a copy of self (List)
        -------------------------------------------------------
        """
        cap = self._count if self._count > 0 else 1
        target = self.__class__(cap)

        i = 0
        while i < self._count:
            target._values[i] = deepcopy(self._values[i])
            i += 1
        target._count = self._count

        return target

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        number = 0
        for i in range(self._count):
            if self._values[i] == key:
                number += 1
        return number

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        index = self._linear_search(key)
        value = None
        if index != -1:
            value = self._values[index]
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list. (int)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        return i

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i is outside the range of -len(list) to len(list) - 1,
        the value is prepended or appended as appropriate.
        Use: source.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._count < len(self._values), "Cannot insert into a full list."

        if i < 0:
            i = 0
        elif i > self._count:
            i = self._count

        for j in range(self._count, i, -1):
            self._values[j] = self._values[j - 1]

        self._values[i] = value
        self._count += 1
        return

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._count == 0, "Target list must be empty."
    
        for i in range(source1._count):
            value = source1._values[i]
            
            in_source2 = False
            for j in range(source2._count):
                if value == source2._values[j]:
                    in_source2 = True
                    break
            already_in_target = False
            for k in range(self._count):
                if value == self._values[k]:
                    already_in_target = True
                    break
            if in_source2 and not already_in_target:
                self._values[self._count] = value
                self._count += 1
    
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        empty = (self._count == 0)

        return empty

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Determines whether two Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        -------------------------------------------------------
        Parameters:
            target - a list (List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equals = (self._count == target._count)
        i = 0
        while equals and i < self._count:
            if self._values[i] != target._values[i]:
                equals = False
            i += 1
        return equals

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._count > 0, 'Cannot find maximum of an empty list'
        value = self._values[0]
        for i in range(1, self._count):
            if self._values[i] > value:
                value = self._values[i]
        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._count > 0, 'Cannot find minimum of an empty list'
        value = self._values[0]
        for i in range(1, self._count):
            if self._values[i] < value:
                value = self._values[i]
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._count > 0, 'Cannot peek at an empty list'

        value = deepcopy(self._values[0])

        return value

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            i = args[0]
            if i < 0:
                i = 0
            elif i >= self._count:
                i = self._count - 1
        else:
            i = self._count - 1

        value = self._values[i]

        for j in range(i + 1, self._count):
            self._values[j - 1] = self._values[j]

        self._count -= 1

        return value

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the list.
        Use: source.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._count < len(self._values), "Cannot prepend to a full list."
    
        
        for i in range(self._count, 0, -1):
            self._values[i] = self._values[i - 1]
    
        
        self._values[0] = deepcopy(value)
        self._count += 1
    
        return

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        index = self._linear_search(key)
        value = None
        if index != -1:
            value = self._values[index]
            for i in range(index, self._count - 1):
                self._values[i] = self._values[i + 1]
            self._values[self._count - 1] = None
            self._count -= 1
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the List.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._count > 0, 'Cannot remove from an empty list'
    
        value = deepcopy(self._values[0])
    
        
        for i in range(1, self._count):
            self._values[i - 1] = self._values[i]
    
        self._count -= 1
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the List that match key.
        Use: source.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        i = 0
        while i < self._count:
            if self._values[i] == key:
                
                for j in range(i + 1, self._count):
                    self._values[j - 1] = self._values[j]
                self._count -= 1
            else:
                i += 1
        return

    def reverse(self):
        """
        -------------------------------------------------------
        The contents of list are reversed in order with respect
        to their order before the operation was called.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        left = 0
        right = self._count - 1

        while left < right:
            self._swap(left, right)
            left += 1
            right -= 1

        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original list (List)
            target2 - a new List with <= 50% of the original list (List)
        -------------------------------------------------------
        """
        cap = self._count if self._count > 0 else 1
        target1 = self.__class__(cap)
        target2 = self.__class__(cap)
    
        mid = (self._count + 1) // 2
        i = 0
        while i < mid:
            target1._values[target1._count] = deepcopy(self._values[i])
            target1._count += 1
            i += 1
        while i < self._count:
            target2._values[target2._count] = deepcopy(self._values[i])
            target2._count += 1
            i += 1
    
        self._count = 0
        return target1, target2
    
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        cap = self._count if self._count > 0 else 1
        target1 = self.__class__(cap)
        target2 = self.__class__(cap)
    
        i = 0
        while i < self._count:
            if i % 2 == 0:
                target1._values[target1._count] = deepcopy(self._values[i])
                target1._count += 1
            else:
                target2._values[target2._count] = deepcopy(self._values[i])
                target2._count += 1
            i += 1
    
        self._count = 0
        return target1, target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        cap = self._count if self._count > 0 else 1
        target1 = self.__class__(cap)
        target2 = self.__class__(cap)

        i = 0
        while i < self._count:
            value = self._values[i]
            if func(value):
                target1._values[target1._count] = deepcopy(value)
                target1._count += 1
            else:
                target2._values[target2._count] = deepcopy(value)
                target2._count += 1
            i += 1

        self._count = 0

        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values < key,
        and target2 contains all values >= key. source is empty
        at end.
        Use: target1, target2 = source.split_key()
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new List of values < key (List)
            target2 - a new List of values >= key (List)
        -------------------------------------------------------
        """
        cap = self._count if self._count > 0 else 1
        target1 = self.__class__(cap)
        target2 = self.__class__(cap)

        i = 0
        while i < self._count:
            value = self._values[i]
            if value < key:
                target1._values[target1._count] = deepcopy(value)
                target1._count += 1
            else:
                target2._values[target2._count] = deepcopy(value)
                target2._count += 1
            i += 1

        self._count = 0

        return target1, target2

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._count == 0, "Target list must be empty."
    
        
        for i in range(source1._count):
            value = source1._values[i]
            found = False
            for j in range(self._count):
                if value == self._values[j]:
                    found = True
                    break
            if not found:
                self._values[self._count] = value
                self._count += 1
    
        
        for i in range(source2._count):
            value = source2._values[i]
            found = False
            for j in range(self._count):
                if value == self._values[j]:
                    found = True
                    break
            if not found:
                self._values[self._count] = value
                self._count += 1
    
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns:
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        i = 0
        while i < self._count:
            value = self._values[i]
            yield value
            i += 1
