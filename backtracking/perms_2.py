class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        # so you add yourself and go next
        # remove yourself and go next

        def bt(idx, subset):
            if idx < len(nums) : 
                # not sure about this 
                subset.append(nums[idx])
                if subset not in result :
                    result.append(tuple(subset))
                bt(idx + 1, subset)
                subset.pop()
                bt(idx + 1, subset)

                # so i'm generating everything correctly just not putting the result in at the right time
                
        bt(0, [])
        return result
