class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m={}
        for i in range(1,len(nums)+1):
            m[i]="F"
        print(m)
        for j in nums:
            if j in m:
                m[j]="T"
        print(m)
        a=[]
        for k in m:
            if m[k]=="F":
                a.append(k)
        return a;