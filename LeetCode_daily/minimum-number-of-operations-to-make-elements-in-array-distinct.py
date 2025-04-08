#3396 Minimum Number of Operations to Make Elements in Array Distinct
# Date: 08/04/2025
# Type: Daily Problem
# Method used: Greedy Approach

from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        while len(nums) != len(set(nums)):  # while duplicates exist
            nums = nums[3:]  # remove first 3 elements
            operations += 1
        
        return operations
