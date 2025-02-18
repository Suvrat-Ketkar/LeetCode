// Write an algorithm to determine if a number n is happy.

// A happy number is a number defined by the following process:

// Starting with any positive integer, replace the number by the sum of the squares of its digits.
// Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy.
// Return true if n is a happy number, and false if not.

#include <unordered_set>
#include <iostream>
using namespace std;

class Solution { 
public:
    bool isHappy(int n) {
        unordered_set<int> set;  // To detect cycles
        int sum_square = n;

        while (sum_square != 1 && set.count(sum_square) == 0) {
            set.insert(sum_square);
            cout << sum_square << " ";  
            sum_square = square_of_digits(sum_square);
        }

        return sum_square == 1;  
    }

    int square_of_digits(int n) {
        int sq = 0;
        while (n != 0) {
            int digit = n % 10;  
            sq += digit * digit;  
            n /= 10;  
        }
        return sq;
    }
};
