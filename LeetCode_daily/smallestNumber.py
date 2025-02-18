#2375 Construct Smallest Number From DI String
# Date: 18/02/2025
#Type: Daily Problem
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []  # Stack to maintain decreasing order
        result = ""  # Final number sequence
        num = 1  # Start with the smallest available number

        for i in range(len(pattern) + 1):
            # Push the number onto the stack
            stack.append(str(num))
            num += 1

            # If we reach an 'I' or the end of the pattern, pop everything from stack
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result += stack.pop()

        return result
