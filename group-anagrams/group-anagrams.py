class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        h={}
        for word in strs:
            sortwords="".join(sorted(word))
            if sortwords not in h:
                h[sortwords]=[word]
            else:
                h[sortwords].append(word)
        print(h)
        final=[]
        for value in h.values():
            final.append(value)
        return final