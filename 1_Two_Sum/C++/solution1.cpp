#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> m;
        
        int len = nums.size();
        for(int i = 0; i < len; ++i)
        {
            if(m.find(target - nums[i]) != m.end())
            {
                return vector<int>{i, m[target - nums[i]]};
            }
            m[nums[i]] = i;
        }
        return std::vector<int>{0, 0};
    }
};