class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            if i in a:
                a[i]=2
            else:
                a[i]=1
        key_list = list(a.keys())
        val_list = list(a.values())
 

        position = val_list.index(1)
        return key_list[position]