#2843 Count Symmetric Integers
# Date: 11/04/2025
# Type: Daily Problem
# Method used: Digit Manipulation

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            digits = []
            temp = num
            while temp:
                digits.append(temp % 10)
                temp //= 10
            digits.reverse()

            if len(digits) % 2 == 0:
                mid = len(digits) // 2
                left_sum = sum(digits[:mid])
                right_sum = sum(digits[mid:])
                if left_sum == right_sum:
                    count += 1

        return count
