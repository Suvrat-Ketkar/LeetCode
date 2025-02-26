#1749 Maximum Absolute Sum of Any Subarray
# Date: 26/02/2025
#Type: Daily Problem
# Method used: Kadane's Algorithm
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum, min_sum = 0, 0  # Maximum and minimum subarray sums
        curr_max, curr_min = 0, 0  # Running max and min subarray sums

        for num in nums:
            curr_max = max(0, curr_max + num)  # Reset if negative
            max_sum = max(max_sum, curr_max)

            curr_min = min(0, curr_min + num)  # Reset if positive
            min_sum = min(min_sum, curr_min)

        return max(max_sum, abs(min_sum))  # Maximum absolute sum

