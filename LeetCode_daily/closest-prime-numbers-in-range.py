# Problem: Closest Prime Numbers in Range
# Date: 07/03/2025
#Type: Daily Problem
# Method used: Sieve of Eratosthenes, Two-Pointer Method
from typing import List
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False 

        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                j = i * i
                while j <= right:
                    sieve[j] = False
                    j += i
        primes = []
        for i in range(left, right + 1):
            if sieve[i]:
                primes.append(i)

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        result = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i], primes[i + 1]]

        return result
