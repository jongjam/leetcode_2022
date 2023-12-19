def characterReplacement(s, k):
    l = 0
    swaps = k
    res = 0
    r = 0
    while r < len(s) :
        if s[r] != s[l] :
            if swaps > 0:
                swaps -= 1
            else :
                swaps = k
                ogl = s[l]

                while s[l] is ogl :
                    l += 1
                r = l
                
        res = max(res, r - l + 1)
        r += 1
    
    return res

# The real solution down here which accounts mismatched chars in the middle of a substring
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        swaps = k
        res = 0
        r = 0
    
        def findMax(dc) :
            return max(dc.values())
        window_letter_count = defaultdict(lambda: 0)
        # windowlen - count[Of most frequent char] = no. of replacements needed
        # if no. of replacements <= k then res = max(res, r - l + 1)
        # if not good enough than move up window until the statement above is valid

        for r in range(len(s)) :
            window_letter_count[s[r]] += 1
            most_freq_char = findMax(window_letter_count)
            window_length = r - l + 1

            while window_length - most_freq_char > k :
                window_letter_count[s[l]] -= 1
                l += 1
                window_length = r - l + 1

            res = max(res, window_length)
        
        
        return res
    


def main() :
    s = "AABABBA"
    s2 = "ABAABBA"
    
    print(characterReplacement(s2, 1))
    
main()