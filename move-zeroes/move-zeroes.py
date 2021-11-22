class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=left+1
        while right<len(nums):
            if nums[left]!=0:
                left+=1
                right+=1
            elif nums[left]==0 and nums[right]==0:
                right+=1
            else:
                nums[left],nums[right]=nums[right],nums[left]