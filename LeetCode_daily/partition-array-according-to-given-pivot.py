#2161 Partition Array According to Given Pivot
# Date: 03/03/2025
#Type: Daily Problem
# Method used: Three-Pass Method
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        part_1 = []
        count = 0
        part_2 = []
        for i in range(0,len(nums)):
            if nums[i] < pivot:
                part_1.append(nums[i])
            elif nums[i] == pivot:
                count += 1
            else:
                part_2.append(nums[i])
        return part_1 + [pivot]*count + part_2
    
        