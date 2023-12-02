class Solution:
    def searchRange(self, nums, target) :
        res = [0] * 2
        res[0] = self.search(nums, target, True)
        res[1] = self.search(nums, target, False)
        return res
    
    def search(self, nums, target, finding_first) :
        l = 0
        r = len(nums) - 1
        # Did not know.... have to find them IN ORDER
        i = -1
        # Trying to find smallest index of target and largest index of target
        while l <= r :
            m = l + (r - l) // 2
            mval = nums[m]
            if mval > target :
                r = m - 1
            elif mval < target :
                l = m + 1
            else :    
                i = m
                if finding_first:
                    r = m - 1 # finds the first
                else :
                    l = m + 1 # finds the last
                # do binary search again 0 to mid (smaller)
                # do binary search again mid to end (bigger)
                # start = min(start, m)
                #     # how to update the bounds
                # end = max(end, m)

                # if we found another eight and 
        return i