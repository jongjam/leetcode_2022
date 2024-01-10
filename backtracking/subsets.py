class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # cinvert deques to list?
        #no duplicates
        #so this means some kind of removal or coming back out
        res = []

        #so add yourself, go next
        #then remove youself, go next
        subset = []
        def bt(idx) :
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums of i
            subset.append(nums[idx])
            bt(idx + 1)

            subset.pop()
            bt(idx + 1)

        
        bt(0)
        return res
