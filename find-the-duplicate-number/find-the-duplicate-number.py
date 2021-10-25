class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m={}
        for i in range(1,len(nums)):
            m[i]=0
        for j in nums:
            m[j]+=1
        for k in m:
            if m[k]>=2:
                return k
            