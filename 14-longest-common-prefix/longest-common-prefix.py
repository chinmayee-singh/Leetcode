class Solution:
    def longestCommonPrefix(self, strs):
        """
        Intuition:
        Sabhi strings me jo starting characters same hain,
        wahi longest common prefix hoga.

        Approach (Horizontal Scanning):
        1. Pehli string ko prefix maan lo.
        2. Baaki har string ke saath compare karo.
        3. Jab tak current string prefix se start nahi hoti,
           prefix ka last character hataate jao.
        4. Agar prefix empty ho gaya → answer "".

        Time Complexity: O(n * m)
            n = number of strings
            m = length of shortest string
            Har string ko prefix se compare karna padta hai.

        Space Complexity: O(1)
            Extra memory use nahi ho rahi (sirf prefix variable).
        """

        # Edge case: empty list
        if not strs:
            return ""

        # Step 1: first string ko prefix maan lo
        prefix = strs[0]

        # Step 2: baaki strings se compare karo
        for s in strs[1:]:

            # Jab tak current string prefix se start nahi hoti
            while not s.startswith(prefix):
                # prefix ko chhota karo
                prefix = prefix[:-1]

                # Agar prefix empty ho gaya → no common prefix
                if prefix == "":
                    return ""

        return prefix
