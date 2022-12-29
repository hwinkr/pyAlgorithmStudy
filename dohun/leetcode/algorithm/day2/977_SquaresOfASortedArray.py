class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums, key = lambda x: abs(x))
        answer = list(map(lambda x: x * x, sorted_nums))
        return answer

nums = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(nums))