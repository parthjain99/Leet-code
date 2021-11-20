import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=collections.Counter(s)
        for i in range(len(s)):
            if a[s[i]]==1:
                return i
        return -1