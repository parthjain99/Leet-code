class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel={}
        count=0
        j=list(jewels)
        for i in j:
            jewel[i]=0
        for s in stones:
            if s in jewel:
                count+=1
        return count