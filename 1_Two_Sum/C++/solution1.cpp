#include <map>
#include <vector>
/**
 * This solution is O(n). Since we only iterate through the given vector once. 
 */
class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        
        std::map<int, int>  *m = new std::map<int, int>;

        int size = nums.size();
        for(int i = 0; i < size; ++i)
        {
            if(m->find(target - nums[i]) != m->end())
            {
                return std::vector<int>{i, (*m)[target - nums[i]]};
            }
            else
            {
                (*m)[nums[i]] = i;
            }
        }
        return std::vector<int>{0, 0};
    }
};