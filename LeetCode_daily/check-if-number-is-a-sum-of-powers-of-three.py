#1780 Check if Number is a Sum of Powers of Three
# Date: 04/03/2025
#Type: Daily Problem
# Method used: Greedy Algorithm

import math

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        used_powers = set()
        while n > 0:
            max_power = int(round(math.log(n, 3)))  # Use round() to fix precision issues
            
            if max_power in used_powers:
                return False
            used_powers.add(max_power)
            n = n - 3**max_power
        return n == 0