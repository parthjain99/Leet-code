  
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res1=nums[0]
        curmin=1
        curmax=1
        for n in nums:
            # if n==0:
            #     curmax=1
            #     curmin=1
            #     continue
            temp=n*curmax  
            curmax=max(n*curmin,n*curmax,n)
            curmin=min(temp,n*curmin,n)
            res1=max(res1,curmin,curmax,n)
        return res1