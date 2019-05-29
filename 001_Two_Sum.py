class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        res = [-1, -1]
        for i, val in enumerate(nums):
            if (target - val) not in dic:
                dic[val] = i
            else:
                res = [dic[target-val], i]

        return res


