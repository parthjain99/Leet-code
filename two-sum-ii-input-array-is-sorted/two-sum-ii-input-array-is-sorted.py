class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a={}
        b=[]
        for i in range(len(numbers)):
            if numbers[i] not in a:
                a[target-numbers[i]]=i+1
            else:
               
                b.append(a[numbers[i]])
                b.append(i+1)
                break
        return b