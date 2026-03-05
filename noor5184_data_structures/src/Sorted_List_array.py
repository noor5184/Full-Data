"""
-------------------------------------------------------
Array version of the Sorted_List ADT.
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-10-11"
-------------------------------------------------------
"""
from copy import deepcopy


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: target = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._values = []


    def __contains__(self, key):
        """
        -------------------------------------------------------
        Determines if source contains key (no Python 'in').
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        lo = 0
        hi = self._count - 1
        found = False
        while not found and lo <= hi:
            mid = (lo + hi) // 2
            if self._values[mid] == key:
                found = True
            elif self._values[mid] < key:
                lo = mid + 1
            else:
                hi = mid - 1
        return found


    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Returns a copy of the nth element of source.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of source (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'
        value = deepcopy(self._values[i])
        return value

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in source.
        -------------------------------------------------------
        """
        # Your code here

        return

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        # Your code here

        return

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(Sorted_List) to len(Sorted_List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return

    def clean(self):
        """
        -------------------------------------------------------
        Removes duplicates from source.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            source contains one and only one of each value formerly present
            in source. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        if self._count <= 1:
            return

        j = 0
        i = 1
        while i < self._count:
            if self._values[i] != self._values[j]:
                j += 1
                self._values[j] = self._values[i]
            i += 1

        self._count = j + 1
        return


    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here

        return

    def copy(self):
        """
        ---------------------------------------------------------
        Copies the contents of this list to another sorted list.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a sorted list containing a copy of the contents 
                of source (Sorted_List)
        -------------------------------------------------------
        """
        # Your code here

        return



    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in source.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in source (int)
        -------------------------------------------------------
        """
        number = 0
        lo = 0
        hi = self._count - 1

        
        while lo <= hi and number == 0:
            mid = (lo + hi) // 2
            if self._values[mid] == key:
                number = 1

                
                i = mid - 1
                while i >= 0 and self._values[i] == key:
                    number += 1
                    i -= 1

                
                i = mid + 1
                while i < self._count and self._values[i] == key:
                    number += 1
                    i += 1
            elif self._values[mid] < key:
                lo = mid + 1
            else:
                hi = mid - 1

        return number


    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        lo = 0
        hi = self._count - 1
        value = None

        
        while lo <= hi and value is None:
            mid = (lo + hi) // 2
            if self._values[mid] == key:
                value = deepcopy(self._values[mid])
            elif self._values[mid] < key:
                lo = mid + 1
            else:
                hi = mid - 1

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        lo = 0
        hi = self._count - 1
        i = -1

        
        while lo <= hi:
            mid = (lo + hi) // 2
            if self._values[mid] == key:
                i = mid
                hi = mid - 1    
            elif self._values[mid] < key:
                lo = mid + 1
            else:
                hi = mid - 1

        return i


    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in source.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here

        return



    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values = []
        self._count = 0

        i = 0
        j = 0

        
        while i < source1._count and j < source2._count:
            if source1._values[i] == source2._values[j]:
                
                if self._count == 0 or self._values[self._count - 1] != source1._values[i]:
                    self._values.append(deepcopy(source1._values[i]))
                    self._count += 1
                i += 1
                j += 1
            elif source1._values[i] < source2._values[j]:
                i += 1
            else:
                j += 1

        return


    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Determines whether two Sorted_Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        -------------------------------------------------------
        Parameters:
            target - a list (Sorted_List)
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
        Returns the maximum value in source.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'
        value = deepcopy(self._values[self._count - 1])
        return value


    def min(self):
        """
        -------------------------------------------------------
        Returns the minimum value in source.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'
        value = deepcopy(self._values[0])
        return value



    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, 'Cannot peek at an empty list'    
        value = deepcopy(self._values[0])
        return value


    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source with index i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], otherwise 
                the last value in source, value is removed from source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value


    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in source
        that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = 0
        value = None

        
        while i < self._count and self._values[i] < key:
            i += 1

        if i < self._count and self._values[i] == key:
            value = deepcopy(self._values[i])
            
            for j in range(i, self._count - 1):
                self._values[j] = self._values[j + 1]
            self._values[self._count - 1] = None
            self._count -= 1

        return value


    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first item in source.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, 'Cannot remove from an empty list'

        value = deepcopy(self._values[0])

        
        for i in range(1, self._count):
            self._values[i - 1] = self._values[i]

        self._values[self._count - 1] = None
        self._count -= 1

        return value


    def remove_many(self, key):
        """
        -------------------------------------------------------
        Removes all values that match key in source.
        Use: source.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - the key to match (?)
        Returns:
            None
        -------------------------------------------------------
        """
        i = 0
        while i < self._count and self._values[i] < key:
            i += 1

        
        start = i
        while i < self._count and self._values[i] == key:
            i += 1

        
        shift = i - start
        for j in range(start, self._count - shift):
            self._values[j] = self._values[j + shift]

        
        for k in range(self._count - shift, self._count):
            self._values[k] = None

        self._count -= shift
        return


    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. source becomes empty.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new list with >= 50% of the original List (Sorted_List)
            target2 - a new list with <= 50% of the original List (Sorted_List)
        -------------------------------------------------------
        """
        mid = self._count // 2 + self._count % 2
        target1 = self.__class__()
        target2 = self.__class__()

        for i in range(mid):
            target1._values.append(deepcopy(self._values[i]))
            target1._count += 1

        for i in range(mid, self._count):
            target2._values.append(deepcopy(self._values[i]))
            target2._count += 1

        
        self._values = []
        self._count = 0

        return target1, target2


    def split_alt(self):
        """
        -------------------------------------------------------
        Split a list into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        source is empty after the function executes.
        (iterative version)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List)
            target2 - the odd indexed elements of the list (Sorted_List)
        -------------------------------------------------------
        """
        target1 = self.__class__()
        target2 = self.__class__()

        for i in range(self._count):
            if i % 2 == 0:
                target1._values.append(deepcopy(self._values[i]))
                target1._count += 1
            else:
                target2._values.append(deepcopy(self._values[i]))
                target2._count += 1

        
        self._values = []
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
        # Your code here

        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all values < key,
        target2 all values >= key. source becomes empty. source is
        empty at end.
        Use: target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new Sorted List with values < key (Sorted_List)
            target2 - a new Sorted List with values >= key (Sorted_List)
        -------------------------------------------------------
        """
        target1 = self.__class__()
        target2 = self.__class__()

       
        i = 0
        while i < self._count and self._values[i] < key:
            target1._values.append(deepcopy(self._values[i]))
            target1._count += 1
            i += 1

        while i < self._count:
            target2._values.append(deepcopy(self._values[i]))
            target2._count += 1
            i += 1

        
        self._values = []
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
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values = []
        self._count = 0

        i = 0
        j = 0

        while i < source1._count and j < source2._count:
            v1 = source1._values[i]
            v2 = source2._values[j]

            if v1 < v2:
                self._values.append(deepcopy(v1))
                self._count += 1
                i += 1
            elif v1 > v2:
                self._values.append(deepcopy(v2))
                self._count += 1
                j += 1
            else:
                
                self._values.append(deepcopy(v1))
                self._count += 1
                i += 1
                j += 1

        
        while i < source1._count:
            self._values.append(deepcopy(source1._values[i]))
            self._count += 1
            i += 1

        while j < source2._count:
            self._values.append(deepcopy(source2._values[j]))
            self._count += 1
            j += 1

        
        source1._values = []
        source1._count = 0
        source2._values = []
        source2._count = 0

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

