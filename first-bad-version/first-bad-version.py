# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        # isbad1=isBadVersion(1)
        # if isbad1==True:
        #     return 1
        # if n==2:            
        #     if isbad1==True:
        #         return 1
        #     else:
        #         return 2
        while left<=right:
            mid=(right+left)//2
            isbad=isBadVersion(mid)                
            if isbad==True:
                if isBadVersion(mid-1):
                    right=mid-1
                else:
                    return mid
            else :
                left=mid+1
            print(mid)
        return mid
                
                
            