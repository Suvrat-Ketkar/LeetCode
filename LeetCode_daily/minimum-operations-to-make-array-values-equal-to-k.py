#3375 Minimum Operations to Make Array Values Equal to K
# Date: 09/04/2025
# Type: Daily Problem
# Method used: Greedy Approach

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1

        # Unique values greater than k
        greater_vals = sorted(set(num for num in nums if num > k), reverse=True)

        # If already all equal to k
        if not greater_vals:
            return 0

        return len(greater_vals)