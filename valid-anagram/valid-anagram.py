class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s="".join(sorted(s))
        t="".join(sorted(t))
        if s==t:
            return True
        else:
            False
        
#         maps={}
#         mapt={}
#         for i in s:
#             maps{i}= maps.get(i,0)+1

#         for i in t:
#             mapt{i}= mapt.get(i,0)+1

        
#         return maps==mapt
                
        
        
        
        
        
#         i=list(s)
#         i.sort()
#         anagram=list(t)
#         anagram.sort()
#         if i==anagram:
#             return True
#         else:
#             return False