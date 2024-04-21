class Solution:
    def longestPalindrome(self, s: str) -> str:
        # longest palindrome is the longest substring palindrome 
        
        # starting from the middle, check if one to the left is good, check one to the right is good
        # check if both
        # isn't this just fucking two pointer FUCK YOU !

        mid =(int)((len(s) - 1) / 2)
        result = s[mid]
        left = mid - 1
        right = mid + 1
        
        def inRange(left, right) :
            return left >= 0 and right < len(s)
        
        while inRange(left, right) :
            left_char = s[left]
            right_char = s[right]
            if left_char == right_char :
                result = left_char + result + right_char
            else :
                if left_char == result[len(result) - 1] :
                    result = left_char + result
                if right_char == result[0] :
                    result = result + right_char
            
            left -= 1
            right += 1
            
            
        return result
