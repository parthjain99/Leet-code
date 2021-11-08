# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        high=n
        flag=True
        while flag:
            mid=low + ((high - low)//2)
            g=guess(mid)
            if g==-1:
                high=mid-1
            elif g==1:
                low=mid+1
            elif g==0:
                flag=False
                return mid
            