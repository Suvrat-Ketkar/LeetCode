#39 Combination sum
# Date: 24/02/2025
# Type: Standard Problem
# Method used: Backtracking


from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current_combination, remaining_target):
            # Base case: if the target is met
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            
            #  no valid combination
            if remaining_target < 0:
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                current_combination.append(candidate)
                backtrack(i, current_combination, remaining_target - candidate)  # Allow repeated usage
                current_combination.pop()  # Undo the choice (backtrack)

        backtrack(0, [], target)
        return result

        