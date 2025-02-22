#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int mid = 0;
        while(low <= high) {
            mid = (high + low) / 2 ;
            if(nums[mid] == target) {
                return mid;
            }
            else if(nums[mid] > target) {
                high = mid - 1;
                
            }
            else {
                low = mid + 1;
            }
        }
        return low;

    }
};