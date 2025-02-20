#1980 Find Unique Binary String    
# Date: 20/02/2025
#Type: Daily Problem

# Method used: diagonal flipping trick (Cantor’s diagonalization). 
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result = []
        
        for i in range(n):
            if nums[i][i] == '1':
                result.append('0')
            else:
                result.append('1')
        
        return ''.join(result)