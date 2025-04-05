# 1863 Sum of All Subset XOR Totals
# Date: 05/04/2025
#Type: Daily Problem
# Method used: Depth First Search

from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [[]]

        # Generate all subsets using loops
        for num in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + [num])  # include num
            subsets.extend(new_subsets)

        total = 0
        for subset in subsets:
            xor_val = 0
            for num in subset:
                xor_val ^= num
            total += xor_val

        return total

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0

        def dfs(index, current_xor):
            if index == len(nums):
                self.total += current_xor
                return
            
            # Include nums[index]
            dfs(index + 1, current_xor ^ nums[index])

            # Exclude nums[index]
            dfs(index + 1, current_xor)

        dfs(0, 0)
        return self.total
