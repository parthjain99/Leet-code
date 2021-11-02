class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h={0:1}
        cursum=0
        res=0        
        for i in nums:
            cursum=cursum+i
            diff=cursum-k
            res+=h.get(diff,0)
            h[cursum]= 1+ h.get(cursum,0)
        return res
            
     