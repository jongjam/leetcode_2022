class Solution:
    # can't do sorting
    # doesn't matter if they are in order
    def longestConsecutive(self, nums: List[int]) -> int:
        # Wait what if put them all into a set or a map because duplicates don't matter

        # My biggest problem right now is... I need a way to know if I just broke a chain
        if len(nums) == 0 :
            return 0

        total_max = 1
        helper = set(nums)

        # The longest consecutive chain can be no longer than the len of nums
        for num in helper :
            if (num - 1) not in helper :
                length = 1
                while num + 1 in helper :
                    length += 1
                    num += 1
                total_max = max(total_max, length)

        return total_max