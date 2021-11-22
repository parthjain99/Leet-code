class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length=len(nums)
        right=0
        ans=[]
        while(right<length and nums[right]<0):
            right+=1
        print(right)
        left=right-1
        while left>=0 and right<length:
            ls=nums[left]**2
            rs=nums[right]**2
            if(ls<rs):
                ans.append(ls)
                left-=1                
            else:
                ans.append(rs)
                right+=1
        while right<=length-1:
            rs=nums[right]**2
            ans.append(rs)
            right+=1
        while left>=0:
            ls=nums[left]**2
            ans.append(ls)
            left-=1
        return ans