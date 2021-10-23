class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        l,r,width=0,len(height)-1,len(height)-1
        for w in range(width,0,-1):
            h=min(height[l],height[r])
            area= w * h
            res=max(res,area)
            print(res)
            if height[r]>height[l]:
                l=l+1
            else:
                r-=1
        return res