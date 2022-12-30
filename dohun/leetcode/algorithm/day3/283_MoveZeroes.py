class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[:] = [num for num in nums if num] + [0 for _ in range(nums.count(0))]

nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))