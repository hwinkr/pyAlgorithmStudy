class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = -1
        start = 0
        end = len(nums) - 1

        while start <= end :
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return answer

nums = [1, 3, 5, 6]
target = 5

print(Solution().search(nums, target))