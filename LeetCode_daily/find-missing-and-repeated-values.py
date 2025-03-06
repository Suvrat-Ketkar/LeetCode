#2965 Find Missing and Repeated Values
# Date: 06/03/2025
#Type: Daily Problem
# Method used: Hashing (Frequency Counting)

from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        num_count = [0] * (n * n + 1)  # Frequency array to track numbers
        repeated, missing = -1, -1

        # Count occurrences of each number
        for row in grid:
            for num in row:
                num_count[num] += 1
        
        # Find the repeated and missing number
        for i in range(1, n * n + 1):
            if num_count[i] == 2:
                repeated = i
            elif num_count[i] == 0:
                missing = i

        return [repeated, missing]

