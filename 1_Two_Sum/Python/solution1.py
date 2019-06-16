class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        attacks = {}
        for i, n in enumerate(nums):
            if target - n in attacks.keys():
                return [i, attacks[target - n]]
            else:
                attacks[n] = i