class Solution(object):
    def twoSum(self, nums, target):
       seen = {} # value : index

       for i, num in enumerate (nums):
            remain = target - num
            if remain in seen: 
                return [seen[remain], i]
            seen[num] = i
        