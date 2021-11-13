class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        ans=[]
        first,last=-1,-1
        while left<=right:
            mid=left+(right-left)//2
            if target==nums[mid]:
                first=mid
                right=mid-1
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if target==nums[mid]:
                last=mid
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return [first,last]
        