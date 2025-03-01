#2460 Apply Operations to an Array
# Date: 01/03/2025
#Type: Daily Problem
# Method used: In-Place Array Manipulation

from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]: 
        for i in range(0,len(nums)-1):
            if(nums[i] == nums[i+1]):
                nums[i] = nums[i]*2
                nums[i+1] = 0
        non_zero = []
        count = 0
        for i in range(0,len(nums)):
            if(nums[i] != 0):
                non_zero.append(nums[i])
            else:
                count += 1
        return non_zero + [0]*count