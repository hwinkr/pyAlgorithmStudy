class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = 0
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
            answer = mid
        if nums[answer] < target:
            return answer + 1
        else:
            return answer