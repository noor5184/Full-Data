""" 
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-11-29"
-------------------------------------------------------
"""
from copy import deepcopy


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        empty = (self._count == 0)
        return empty


    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        n = self._count
        return n


    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _List_Node(value, self._front)
        self._front = node
        if self._rear is None:
            self._rear = node
        self._count += 1
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _List_Node(value, None)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear._next = node
            self._rear = node
        self._count += 1
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._front is None or i <= -self._count:
            self.prepend(value)
        elif i >= self._count:
            self.append(value)
        else:
            n = i + self._count if i < 0 else i

            if n == 0:
                self.prepend(value)
            else:
                previous = self._front
                index = 1

                while index < n:
                    previous = previous._next
                    index += 1

                node = _List_Node(value, previous._next)
                previous._next = node

                if node._next is None:
                    self._rear = node

                self._count += 1
        return


    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key is not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0
        found = False

        while current is not None and not found:
            if current._value == key:
                found = True
            else:
                previous = current
                current = current._next
                index += 1

        if not found:
            previous = None
            current = None
            index = -1
        return previous, current, index


    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, index = self._linear_search(key)
        value = None

        if current is not None:
            value = current._value
            if previous is None:
                self._front = current._next
                if self._front is None:
                    self._rear = None
            else:
                previous._next = current._next
                if previous._next is None:
                    self._rear = previous
            self._count -= 1
        return value


    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        node = self._front
        self._front = node._next
        if self._front is None:
            self._rear = None
        self._count -= 1
        value = node._value
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        prev = None
        cur = self._front
        while cur is not None:
            if cur._value == key:
                if prev is None:
                    self._front = cur._next
                    if self._front is None:
                        self._rear = None
                else:
                    prev._next = cur._next
                    if prev._next is None:
                        self._rear = prev
                self._count -= 1
                cur = self._front if prev is None else prev._next
            else:
                prev = cur
                cur = cur._next
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, index = self._linear_search(key)

        if current is None:
            value = None
        else:
            value = deepcopy(current._value)
        return value


    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        value = deepcopy(self._front._value)
        return value


    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        previous, current, i = self._linear_search(key)
        return i


    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        n = i + self._count if i < 0 else i
        j = 0
        current = self._front
        while j < n:
            current = current._next
            j += 1
        value = deepcopy(current._value)
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        n = i + self._count if i < 0 else i
        j = 0
        current = self._front

        while j < n:
            current = current._next
            j += 1

        current._value = deepcopy(value)
        return


    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        previous, current, index = self._linear_search(key)
        found = (current is not None)
        return found


    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        max_data = current._value
        current = current._next

        while current is not None:
            if current._value > max_data:
                max_data = current._value
            current = current._next

        max_data = deepcopy(max_data)
        return max_data


    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        min_data = current._value
        current = current._next

        while current is not None:
            if current._value < min_data:
                min_data = current._value
            current = current._next

        min_data = deepcopy(min_data)
        return min_data


    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        number = 0
        current = self._front

        while current is not None:
            if current._value == key:
                number += 1
            current = current._next
        return number


    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        self._rear = self._front

        while current is not None:
            nxt = current._next
            current._next = previous
            previous = current
            current = nxt

        self._front = previous
        return


    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        self._rear = self._front

        def _reverse(cur, prev):
            if cur is None:
                result = prev
            else:
                nxt = cur._next
                cur._next = prev
                result = _reverse(nxt, cur)
            return result

        self._front = _reverse(self._front, None)
        return


    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        prev = None
        cur = self._front
        while cur is not None:
            runner_prev = cur
            runner = cur._next
            while runner is not None:
                if runner._value == cur._value:
                    runner_prev._next = runner._next
                    if runner_prev._next is None:
                        self._rear = runner_prev
                    self._count -= 1
                    runner = runner_prev._next
                else:
                    runner_prev = runner
                    runner = runner._next
            prev = cur
            cur = cur._next
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
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
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next 
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                left = self._front
                self._front = prn._next
            else:
                left = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                right = self._front
                self._front = left
            else:
                right = prn._next
                prn._next = left

            # Swap next pointers
            # lst._next, r._next = r._next, lst._next
            temp = left._next
            left._next = right._next
            right._next = temp
            # Update the rear
            if right._next is None:
                self._rear = right
            elif left._next is None:
                self._rear = left
        return

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
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

    def identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        def _ident(a, b):
            if a is None and b is None:
                result = True
            elif a is None or b is None:
                result = False
            elif a._value != b._value:
                result = False
            else:
                result = _ident(a._next, b._next)
            return result

        if self._count == other._count:
            identical = _ident(self._front, other._front)
        else:
            identical = False
        return identical


    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        first_half = (self._count + 1) // 2

        i = 0
        while self._front is not None and i < first_half:
            node = self._front
            self._front = node._next
            if self._front is None:
                self._rear = None
            node._next = None
            if target1._rear is None:
                target1._front = node
                target1._rear = node
            else:
                target1._rear._next = node
                target1._rear = node
            target1._count += 1
            self._count -= 1
            i += 1

        while self._front is not None:
            node = self._front
            self._front = node._next
            if self._front is None:
                self._rear = None
            node._next = None
            if target2._rear is None:
                target2._front = node
                target2._rear = node
            else:
                target2._rear._next = node
                target2._rear = node
            target2._count += 1
            self._count -= 1

        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source self is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        toggle = True

        while self._front is not None:
            node = self._front
            self._front = node._next
            if self._front is None:
                self._rear = None
            node._next = None

            if toggle:
                if target1._rear is None:
                    target1._front = node
                    target1._rear = node
                else:
                    target1._rear._next = node
                    target1._rear = node
                target1._count += 1
            else:
                if target2._rear is None:
                    target2._front = node
                    target2._rear = node
                else:
                    target2._rear._next = node
                    target2._rear = node
                target2._count += 1

            self._count -= 1
            toggle = not toggle

        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty.
        Order of even and odd is not significant.
        (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        even = List()
        odd = List()

        def _split(source, even, odd, toggle):
            if source._front is None:
                return
            node = source._front
            source._front = node._next
            if source._front is None:
                source._rear = None
            node._next = None

            target = even if toggle else odd

            if target._rear is None:
                target._front = node
                target._rear = node
            else:
                target._rear._next = node
                target._rear = node
            target._count += 1
            source._count -= 1

            _split(source, even, odd, not toggle)

        _split(self, even, odd, True)
        return even, odd


    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        def _search(prev, cur, index):
            if cur is None:
                result = (None, None, -1)
            elif cur._value == key:
                result = (prev, cur, index)
            else:
                result = _search(cur, cur._next, index + 1)
            return result

        previous, current, index = _search(None, self._front, 0)
        return previous, current, index


    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

        a = source1._front
        while a is not None:
            in_b = False
            b = source2._front
            while (not in_b) and b is not None:
                if a._value == b._value:
                    in_b = True
                else:
                    b = b._next
            if in_b:
                exists = False
                t = self._front
                while (not exists) and t is not None:
                    if t._value == a._value:
                        exists = True
                    else:
                        t = t._next
                if not exists:
                    node = _List_Node(a._value, None)
                    if self._rear is None:
                        self._front = node
                        self._rear = node
                    else:
                        self._rear._next = node
                        self._rear = node
                    self._count += 1
            a = a._next
        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

        def in_list(node, value):
            while node is not None:
                if node._value == value:
                    found = True
                    return found
                node = node._next
            found = False
            return found

        def add_if_new(value):
            if value not in self:
                node = _List_Node(value, None)
                if self._rear is None:
                    self._front = node
                    self._rear = node
                else:
                    self._rear._next = node
                    self._rear = node
                self._count += 1
            return

        def _intersect(node):
            if node is not None:
                if in_list(source2._front, node._value):
                    add_if_new(node._value)
                _intersect(node._next)
            return

        _intersect(source1._front)
        return


    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

        def add_if_new(val):
            exists = False
            c = self._front
            while (not exists) and c is not None:
                if c._value == val:
                    exists = True
                else:
                    c = c._next
            if not exists:
                node = _List_Node(val, None)
                if self._rear is None:
                    self._front = node
                    self._rear = node
                else:
                    self._rear._next = node
                    self._rear = node
                self._count += 1

        a = source1._front
        while a is not None:
            add_if_new(a._value)
            a = a._next

        b = source2._front
        while b is not None:
            add_if_new(b._value)
            b = b._next

        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

        def add_if_new(value):
            if value not in self:
                node = _List_Node(value, None)
                if self._rear is None:
                    self._front = node
                    self._rear = node
                else:
                    self._rear._next = node
                    self._rear = node
                self._count += 1
            return

        def _add_from(node):
            if node is not None:
                add_if_new(node._value)
                _add_from(node._next)
            return

        _add_from(source1._front)
        _add_from(source2._front)
        return


    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        def _clean(node):
            if node is not None:
                runner_prev = node
                runner = node._next

                while runner is not None:
                    if runner._value == node._value:
                        runner_prev._next = runner._next
                        if runner_prev._next is None:
                            self._rear = runner_prev
                        self._count -= 1
                        runner = runner_prev._next
                    else:
                        runner_prev = runner
                        runner = runner._next
                _clean(node._next)
            return

        if self._front is not None:
            _clean(self._front)
        return


    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()

        if self._front is not None:
            slow = self._front
            fast = self._front
            prev = None

            while fast is not None and fast._next is not None:
                prev = slow
                slow = slow._next
                fast = fast._next._next

            if prev is not None:
                prev._next = None

            target1._front = self._front
            target2._front = slow if prev is not None else None

            def _fix(lst):
                current = lst._front
                last = None
                count = 0
                while current is not None:
                    last = current
                    current = current._next
                    count += 1
                lst._rear = last
                lst._count = count
                return

            _fix(target1)
            _fix(target2)

        self._front = None
        self._rear = None
        self._count = 0
        return target1, target2


    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish, self
        is empty.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()

        while self._front is not None:
            node = self._front
            self._front = node._next
            if self._front is None:
                self._rear = None
            node._next = None

            if node._value <= key:
                dest = target1
            else:
                dest = target2

            if dest._rear is None:
                dest._front = node
                dest._rear = node
            else:
                dest._rear._next = node
                dest._rear = node
            dest._count += 1
            self._count -= 1
        return target1, target2


    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        new_list = List()
        current = self._front

        while current is not None:
            new_list.append(current._value)
            current = current._next
        return new_list


    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        new_list = List()

        def _copy(node):
            if node is not None:
                new_list.append(node._value)
                _copy(node._next)
            return

        _copy(self._front)
        return new_list


    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the front
        of the current List. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        source._front = node._next
        if source._front is None:
            source._rear = None
        source._count -= 1

        node._next = self._front
        self._front = node
        if self._rear is None:
            self._rear = node
        self._count += 1
        return


    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        source._front = node._next
        if source._front is None:
            source._rear = None
        source._count -= 1

        node._next = None
        if self._rear is None:
            self._front = node
            self._rear = node
        else:
            self._rear._next = node
            self._rear = node
        self._count += 1
        return


    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        turn = 0
        while source1._front is not None or source2._front is not None:
            take_from_1 = ((turn % 2 == 0) and source1._front is not None) or (source2._front is None)
            src = source1 if take_from_1 else source2

            node = src._front
            src._front = node._next
            if src._front is None:
                src._rear = None
            node._next = None

            if self._rear is None:
                self._front = node
                self._rear = node
            else:
                self._rear._next = node
                self._rear = node

            self._count += 1
            src._count -= 1
            turn += 1
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        def _combine(src1, src2, turn):
            if src1._front is None and src2._front is None:
                return

            take_from_1 = ((turn % 2 == 0) and src1._front is not None) or (src2._front is None)
            src = src1 if take_from_1 else src2

            node = src._front
            src._front = node._next
            if src._front is None:
                src._rear = None
            src._count -= 1
            node._next = None

            if self._rear is None:
                self._front = node
                self._rear = node
            else:
                self._rear._next = node
                self._rear = node
            self._count += 1

            _combine(src1, src2, turn + 1)
            return

        _combine(source1, source2, 0)
        return

    
    
    
    def clear(self):
        """
        -------------------------------------------------------
        Clears the contents of the list.
        Use: source.clear()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        
        self.clean()
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
