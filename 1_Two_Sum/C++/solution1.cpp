#include <map>
<<<<<<< HEAD

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
=======
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
>>>>>>> ef5115d327ec083c97cf63508faac3dc413363c1
        }
        return std::vector<int>{0, 0};
    }
};