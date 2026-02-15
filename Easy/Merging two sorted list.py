class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        Intuition:
        Since both linked lists are already sorted,
        we can merge them by always choosing the smaller current node.

        Approach:
        1. Create a dummy node to simplify edge cases.
        2. Use a pointer (current) to build the merged list.
        3. Compare values of list1 and list2:
           - Attach the smaller node to current.
           - Move that list's pointer forward.
        4. When one list becomes empty,
           attach the remaining part of the other list.
        5. Return dummy.next (start of merged list).

        Time Complexity: O(n + m)
            - We traverse both lists once.

        Space Complexity: O(1)
            - No extra memory used (in-place merge).
        """

        # Step 1: create dummy node
        dummy = ListNode(0)
        current = dummy

        # Step 2: traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Step 3: attach remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Step 4: return merged list
        return dummy.next
