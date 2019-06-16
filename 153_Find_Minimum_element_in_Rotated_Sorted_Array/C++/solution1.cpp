#include <vector>

class Solution {
public:
    int findMin(vector<int>& nums) {
        if(nums.size() < 2){
            return nums[0];
        }
        
        int prev = nums[0];
        int len = nums.size();
        for(int i = 1; i < len; ++i)
        {
            if(nums[i] < prev){
                return nums[i];
            }
            prev = nums[i];
        }
        return nums[0];
    }
};