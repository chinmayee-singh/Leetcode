class Solution:
    def isValid(self, s):
        """
        Intuition:
        Every opening bracket must be closed by the same type of bracket,
        and the most recently opened bracket must be closed first.
        This follows the Stack (LIFO) principle.

        Approach:
        1. Create an empty stack.
        2. Traverse the string from left to right.
        3. If an opening bracket appears → push it onto the stack.
        4. If a closing bracket appears:
           - If the stack is empty → invalid.
           - Pop the top element and check if it matches.
           - If not matching → invalid.
        5. At the end, if the stack is empty → valid parentheses.

        Time Complexity: O(n)
            Each character is processed once.

        Space Complexity: O(n)
            In the worst case, all opening brackets are stored in the stack.
        """

        stack = []

        # Mapping of closing brackets to their corresponding opening brackets
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            # If it is a closing bracket
            if ch in mapping:
                # Pop the top element if stack is not empty, else use dummy value
                top = stack.pop() if stack else '#'

                # If brackets do not match → invalid
                if mapping[ch] != top:
                    return False
            else:
                # Opening bracket → push onto stack
                stack.append(ch)

        # If stack is empty → valid parentheses
        return not stack
