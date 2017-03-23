class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pair = {}
        idx_list = []

        for idx,n in enumerate(nums):
            val = target - n
            if val in pair:
                idx_list.append(pair[val])
                idx_list.append(idx)
                break
            else:
                   pair[n] = idx
        return idx_list

s = Solution()
nums = [-1,-2,-3,-4,-5]
target = -8
print s.twoSum(nums, target)
