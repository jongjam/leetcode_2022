class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sort_strs = []
        a_map = defaultdict(list) # dictionary initialized 

        # I have to go through 1 time to sorted each one

        for s in strs :
            sort_strs.append("".join(sorted(s)))

        # Now that they are sorted we can tell they are anagrams with ==

        for i in range(len(sort_strs)) :
            string = sort_strs[i]
            if string in a_map :
                a_map[string].append(i)
            else :
                a_map[string] = [i]

        for key in a_map.keys() :
            cur = a_map[key]
            cur_list = [] * len(cur)
            for i in cur :
                cur_list.append(strs[i])
            result.append(cur_list)
                
        # Keep track of the indexes certain anagrams are at so I can add them to the result at the end...
        # Use map... find indexes... add indexes done
        

        return result