import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=0
        sum=0
        maxn=-sys.maxsize
        print(maxn)
        for i in range(len(nums)):
            if sum + nums[i]>0:
                sum+=nums[i]
            else:
                sum=0
            ans= max(sum,ans)
        if ans==0:
            for i in range(len(nums)):
                if nums[i]>maxn:
                    maxn=nums[i]
            ans=maxn
        return ans