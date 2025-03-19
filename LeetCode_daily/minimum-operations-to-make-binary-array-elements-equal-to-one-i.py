#3191 Minimum Operations to Make Binary Array Elements Equal to One I
# Date: 19/03/2025
#Type: Daily Problem
# Method used: Sliding Window

from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        l = len(nums)
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                count += 1
        if(nums[l-1] + nums[l-2] == 2):
            return count
        else:
            return -1