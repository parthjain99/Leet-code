class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeated,recorded=set(),set()
        for i in range(len(s)-9):
            substring=s[i:i+10]
            if substring in recorded:
                repeated.add(substring)
            else:
                recorded.add(substring)
        return list(repeated)