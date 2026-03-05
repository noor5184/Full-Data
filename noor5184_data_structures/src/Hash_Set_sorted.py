"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-07-27"
-------------------------------------------------------
"""
from Sorted_List_linked import Sorted_List

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20


    def __init__(self, capacity):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of given capacity.
        Use: hs = Hash_Set(capacity)
        -------------------------------------------------------
        Parameters:
            capacity - number of slots in the hash set (int > 0)
        Returns:
            A Hash_Set object.
        -------------------------------------------------------
        """
        assert capacity > 0, "Capacity must be > 0"
        self._capacity = capacity
        self._table = [Sorted_List() for _ in range(self._capacity)]
        self._count = 0
        
        
    def _hash(self, key):
        """
        -------------------------------------------------------
        Generates a hash value for key.
        Use: index = self._hash(key)
        -------------------------------------------------------
        Parameters:
            key - a key object (must be hashable)
        Returns:
            index - the hash value for key (int)
        -------------------------------------------------------
        """
        return hash(key) % self._capacity
        
    
    

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot list where the key should go.
        Use: slot = hs._find_slot(key)
        -------------------------------------------------------
        Parameters:
            key - the value to hash (?)
        Returns:
            slot - list at the hash key index (List)
        -------------------------------------------------------
        """
        index = hash(key) % self._capacity
        return self._table[index]

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        ---------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        ---------------------------------------------------------
        """
        slot = self._find_slot(key)
        
        return key in slot
    

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value into the Sorted_List bucket for its hash slot.
        If the word already exists in the slot, just update .comparisons.
        -------------------------------------------------------
        Parameters:
            value - a Word object
        Returns:
            None
        -------------------------------------------------------
        """
        slot_index = self._hash(value)
        slot       = self._table[slot_index]
    
        # Look for an existing copy of value in the slot.
        found = False
        for existing in slot:              # Sorted_List is iterable
            if existing == value:          
                existing.comparisons += value.comparisons
                found = True
                break                      # stop scanning – we updated it
    
        
        if not found:
            slot.insert(value)            
            self._count += 1
    
        return



            
        

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        ---------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        ---------------------------------------------------------
        """
        slot = self._find_slot(key)
        for item in slot:
            if item == key:
                return item
        return None

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        ---------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        ---------------------------------------------------------
        """
        slot = self._find_slot(key)
        for i in range(len(slot)):
            if slot[i] == key:
                value = slot.pop(i)
                self._count -= 1
                return value
        return None

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        ---------------------------------------------------------
        Returns:
            None
        ---------------------------------------------------------
        """
        old_table = self._table
        self._capacity = self._capacity * 2 + 1
        self._table = [Sorted_List() for _ in range(self._capacity)]
        self._count = 0

        for slot in old_table:
            for value in slot:
                value.comparisons = 1
                self.insert(value)

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Hash_Sets are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------------------------------------------------
        Parameters:
            target - a hash set (Hash_Set)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------------------------------------------------
        """
        if self._count != target._count:
            return False
        for i in range(self._capacity):
            if self._table[i] != target._table[i]:
                return False
        return True

    def debug(self):
        """
        ---------------------------------------------------------
        USE FOR TESTING ONLY
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed.
        Use: hs.debug()
        ---------------------------------------------------------
        Returns:
            None
        ---------------------------------------------------------
        """
        for i, slot in enumerate(self._table):
            print(f"{i:2}: ", end='')
            for value in slot:
                print(f"{value}", end=' ')
            print()
            
            
    


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item
