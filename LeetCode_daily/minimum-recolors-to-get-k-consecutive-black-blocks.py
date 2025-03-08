#2379 Minimum Recolors to Get K Consecutive Black Blocks
# Date: 08/03/2025
#Type: Daily Problem
# Method used: Sliding Window

from typing import List
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = blocks[0:k].count('W')
        current_operations = min_operations

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_operations -= 1

            if blocks[i] == 'W':
                current_operations += 1
                
            min_operations = min(min_operations, current_operations)

        return min_operations