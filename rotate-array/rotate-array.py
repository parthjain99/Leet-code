class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        k=k%len(nums)
        start=0
        end=len(nums)-1
        helper(start,end)
        helper(start,k-1)
        helper(k,end)