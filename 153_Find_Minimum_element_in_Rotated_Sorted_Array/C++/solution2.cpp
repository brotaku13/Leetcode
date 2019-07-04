class Solution {
public:
    int findMin(vector<int>& nums) {
        // if there is only one element in the array
        if(nums.size() == 1)
            return nums[0];

        //init right and left pointers
        int left = 0, right = nums.size() - 1;

        // if the last element, is greater than the first element, 
        // then there is no rotation 
        if(nums[0] < nums[right])
            return nums[left];

        int mid;
        //binary search
        while(right >= left)
        {
            //find mid element
            mid = left + (right - left) / 2;

            //if mid element is greater than its next element then mid+1 is the point of change
            if(nums[mid] > nums[mid + 1])
                return nums[mid + 1];

            if(nums[mid] < nums[mid - 1])
                return nums[mid];

            // if the mid value is greator than the left value, then 
            // this means the smallest value is still somewhere to the right 
            // since we are still dealing with elements greater than nums[0]
            if(nums[mid] > nums[0])
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }       
        }
        return -1;
    }
};