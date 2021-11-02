class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        c_list=sorted(freq, key=lambda item: freq[item],reverse=True)
        ans=[]
        for i in c_list:
            ans.append(i*freq[i])
        return "".join(ans)
            