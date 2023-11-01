class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_map = defaultdict(list) # dictionary initialized 
        for s in strs :
            string = "".join(sorted(s))
            if string in a_map :
                a_map[string].append(s)
            else :
                a_map[string] = [s]


        # Now that they are sorted we can tell they are anagrams with ==

       
        # Keep track of the indexes certain anagrams are at so I can add them to the result at the end...
        # Use map... find indexes... add indexes done


        return list(a_map.values())