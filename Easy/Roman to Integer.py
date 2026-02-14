class Solution:
    def romanToInt(self, s):
        """
        Intuition:
        Roman numerals usually add values from left to right.
        But if a smaller value comes before a larger value,
        we subtract instead of add (e.g., IV = 5 - 1 = 4).

        Approach:
        1. Store Roman symbol values in a dictionary.
        2. Traverse the string from left to right.
        3. If current value < next value → subtract.
           Else → add.
        4. Keep summing to get final integer.

        Time Complexity: O(n)
            - We traverse the string once.

        Space Complexity: O(1)
            - Dictionary size is constant (fixed 7 symbols).
        """

        # Step 1: Roman symbol → integer mapping
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # final answer

        # Step 2: traverse string
        for i in range(len(s)):

            # If next value is greater → subtract current
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total
