class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Using the hackey way with arrays
        # If it contained unicode characters I would just make my array size 94 (all symbols on ekyboard) and minus each character by 32

        # I go O(n) runtime and then memory is O(amount of characters checked so)
        if (len(s) != len(t)) :
            return False
        
        # Count of letters
        chars = [0] * 26 
        # ascii value of a is 97
        
        # We know that they are same size now so it is okay to just use 1
        for i in range(len(s)) :
            t_letter = ord(t[i]) - 97
            s_letter = ord(s[i]) - 97
            chars[s_letter] += 1
            chars[t_letter] -= 1
        
        #If they are all not zero then we know that there is a difference in letters between the two

        for i in chars :
            if i != 0 :
                return False
        
        return True



        