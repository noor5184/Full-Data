"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-10-04"
-------------------------------------------------------
"""
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, prev_, next_):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, prev_, next_)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            prev_ - another deque node (_Deque_Node)
            next_ - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = prev_
        self._next = next_


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        empty = (self._count == 0)
        return empty

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        n = self._count
        return n

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Deques are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a deque (Deque)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------"""
        equals = False

        if self._count == target._count:
            a = self._front
            b = target._front
            same = True

            while same and a is not None:
                if a._value != b._value:
                    same = False
                else:
                    a = a._next
                    b = b._next
            equals = same
        return equals

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, None, self._front)

        if self._front is None:
            self._rear = node
        else:
            self._front._prev = node

        self._front = node
        self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, self._rear, None)

        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._count += 1
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"

        node = self._front
        self._front = node._next

        if self._front is None:
            self._rear = None
        else:
            self._front._prev = None

        self._count -= 1
        value = node._value
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"

        node = self._rear
        self._rear = node._prev

        if self._rear is None:
            self._front = None
        else:
            self._rear._next = None

        self._count -= 1
        value = node._value
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"

        value = deepcopy(self._front._value)
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"

        value = deepcopy(self._rear._value)
        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"

        if l is not r:
            if r._next is l:
                l, r = r, l

            if l._next is r:
                l_prev = l._prev
                r_next = r._next

                r._prev = l_prev
                if l_prev is not None:
                    l_prev._next = r
                else:
                    self._front = r

                r._next = l
                l._prev = r
                l._next = r_next

                if r_next is not None:
                    r_next._prev = l
                else:
                    self._rear = l
            else:
                l_prev = l._prev
                l_next = l._next
                r_prev = r._prev
                r_next = r._next

                if l_prev is not None:
                    l_prev._next = r
                else:
                    self._front = r

                if l_next is not None:
                    l_next._prev = r

                if r_prev is not None:
                    r_prev._next = l
                else:
                    self._front = l

                if r_next is not None:
                    r_next._prev = l

                l._prev, r._prev = r_prev, l_prev
                l._next, r._next = r_next, l_next

                if self._rear is l:
                    self._rear = r
                elif self._rear is r:
                    self._rear = l
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
