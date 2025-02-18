// The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
// such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
// F(0) = 0, F(1) = 1
// F(n) = F(n - 1) + F(n - 2), for n > 1.
// Given n, calculate F(n).


class Solution {
public:
    int fib(int n) {
        int n1 = 0;
        int n2 = 1;
        int cur = 0;
        for(int i = 0;i<n;i++) {
            cur = n1 + n2;
            n1 = n2;
            n2 = cur;
        }
        
        return n1;
    }
};