class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        seen = set()
 

        for l in range(len(s) - 9) :
            substring = s[l:l + 10]
            if substring in seen :
                res.add(substring) # Problem,, only had shit you have seen once!
            
            seen.add(substring)

        return list(res)