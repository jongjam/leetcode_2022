from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2) :
        # a permutation is just another way to write a string
        # keep moving r window as long as s2[r] is in set of s1
        # and the occurence of s2[r] iis not greater than letter cout in s1
        l = 0
        r = 2
        counts_s1 = Counter(s1)
        counts+
         # window length

        
        # r = l + 1 will not work in the case that s1 = "a" and s2 = "bcda"

        while l < len(s2) :
            if s2[l] in counts_s1 :
                r = l
                helper_counts = dict(counts_s1) # s1 clone, everytime s2[r] is in s1 we will subtract that 
                # key by 1. if all counts in the clone are 0, we found a permutation, otherwise
                #l can be updated to r

                cur_chain_length = 0
                while r < len(s2) and s2[r] in counts_s1: # I'm not sure if this is right... 
                    # should not have issues with being present here
                    if cur_chain_length > len(s1) :
                        break

                    helper_counts[s2[r]] = max(0, helper_counts[s2[r]] - 1)
                    r += 1
                    cur_chain_length += 1
                    
                if all(value == 0 for value in helper_counts.values()) :
                    return True
                else :
                    l = r + 1
            else :
                l += 1


        return False