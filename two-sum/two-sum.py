class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,val in enumerate(nums):
            y=target-val
            if y in a:
                z=a[y]
                return(z,i)
            else:
                a[val]=i
            
            