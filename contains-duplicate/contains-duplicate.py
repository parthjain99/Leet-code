class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups=set()
        for i in range(len(nums)):
            if nums[i] in dups:
                return True
            else:
                dups.add(nums[i])
        return False