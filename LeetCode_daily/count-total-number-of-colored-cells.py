#2579 Count Total Number of Colored Cells
# Date: 05/03/2025
#Type: Daily Problem
# Method used: Arithmetic Progression

from typing import List

class Solution:
    def coloredCells(self, n: int) -> int:
        m =  1 + (n-1)*2
        S = int(n/2*(2 + (n-1)*2))
        return 2*S - m
