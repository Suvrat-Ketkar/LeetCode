#2780 Minimum Index of a Valid Split
# Date: 2272/03/2025
#Type: Daily Problem
# Method used: Boyer-Moore’s Voting Algorithm

from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the dominant element using Boyer-Moore's algorithm
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Step 2: Count occurrences of the dominant element
        total_count = nums.count(candidate)
        left_count = 0  # Count of dominant element in the left partition

        # Step 3: Find the minimum valid index
        for i in range(len(nums) - 1):
            if nums[i] == candidate:
                left_count += 1
            right_count = total_count - left_count

            # Check if the dominant condition holds in both parts
            if left_count * 2 > (i + 1) and right_count * 2 > (len(nums) - i - 1):
                return i  # Minimum index found

        return -1  # No valid split found
