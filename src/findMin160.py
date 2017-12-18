class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        length = len(nums)
        ret = nums[0]

        if len == 1:
            return ret

        for i in range(1,length):
            if nums[i] < ret:
                ret = nums[i]

        return ret

solution = Solution()
print solution.findMin([4, 4, 5, 6, 7, 0, 1, 2])