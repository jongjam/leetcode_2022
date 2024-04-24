class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0
        def in_range(l, r) :
            return l >= 0 and r < len(s)

        for i in range(len(s)) :
            # Even length
            l, r = i, i
            while in_range(l, r) and s[l] == s[r] :
                if (r - l + 1) > resLen :
                    result = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # Uneven length
            l, r = i, i + 1 # starting one over so let's say it starts at 
            # i = 1, first b in example 2
            # going r = i + 1
            # will look at bb and then call it good 
            while in_range(l, r) and s[l] == s[r] :
                if (r - l + 1) > resLen :
                    result = s[l:r + 1]
                    resLen = r - l + 1
                    print(resLen)
                    print(len(result))
                l -= 1
                r += 1

        return result
