class Solution:
    def isValid(self, s: str) -> bool:
       stack=["N"]
       dict={"]":"[","}":"{",")":"("}
       for i in s:
            if i in dict.keys():
                if dict[i]!=stack.pop():
                    return False
            else:
                stack.append(i)
       return len(stack)==1