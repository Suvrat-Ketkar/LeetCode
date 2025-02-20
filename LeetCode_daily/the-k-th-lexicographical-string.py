#1415 The k-th Lexicographical String of All Happy Strings of Length n
# Date: 19/02/2025
#Type: Daily Problem
# Method used: Recursion
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def find_happy_string(length, k, last_char):
            if length == 0:
                return ""
            
            total_per_branch = 2 ** (length - 1)  # Remaining possible strings per group
            if k > 3 * total_per_branch:  # If k is out of range
                return ""
            
            # Determine which character should be placed at this position
            candidates = ['a', 'b', 'c']
            if last_char in candidates:
                candidates.remove(last_char)  # Remove the last character to maintain happy string condition
            
            # Find which group `k` belongs to and recurse
            for i, char in enumerate(candidates):
                if k <= (i + 1) * total_per_branch:
                    return char + find_happy_string(length - 1, k - i * total_per_branch, char)
            
            return ""

        return find_happy_string(n, k, "")


