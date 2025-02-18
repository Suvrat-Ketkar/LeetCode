// Problem Statement
// You are climbing a staircase with n steps. At each step, you can either climb 1 or 2 steps. 
// Your task is to determine the number of distinct ways you can climb to the top.


class Solution {
public:
    int climbStairs(int n) {
        if (n<=3) {
            return n;
        }
        int n1 = 2;
        int n2 = 3;
        int cur = 0;
        for(int i = 3;i<n;i++) {
            cur = n1 + n2;
            n1 = n2;
            n2 = cur;
        }
        return cur;
    }
};