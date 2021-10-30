class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        b=[]
        for i in range(len(nums)):
            if nums[i] in a:
                a[nums[i]]+=1   
            else:
                a[nums[i]]=1
        i=0
        while k>0:
            maxval=max(a,key=a.get)
            b.append(maxval)
            a[maxval] =0
            k -=1
            i+=1
        return b