// wow this is naive. It's from a long time ago, give me a break. 

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> m = new HashMap();
        boolean found = false;
        int[] ret = new int[2];
        
        for(int i = 0; i < nums.length && !found; ++i){
            if(m.containsKey(target - nums[i])){
                ret[0] = m.get(target - nums[i]);
                ret[1] = i;
            } else {
                m.put(nums[i], i);
            }
        }
        
        return ret;
    }
}