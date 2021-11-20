class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        occur={}
        for i in nums1:
            if i in occur:
                occur[i]+=1
            else:
                occur[i]=1
        
        
        ans=[]
        for i in nums2:
            if i in occur and occur[i]>0:
                ans.append(i)
                occur[i]-=1
        return ans