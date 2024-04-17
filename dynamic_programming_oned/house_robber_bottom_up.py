class Solution:
    def rob(self, nums: List[int]) -> int:
        # maximum sum from non adjacent index
        # this seems like a good opportunity to start from the very end
        # but this isn't really a fibonnaci because there isn't a set number of spaces or steps needed

        # but if we start at the very end
        # the max sum is the end idx
        print(nums)
        nums.append(0)
        # why does this one work
        for i in range(len(nums) - 3, -1, -1) :
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
        # the problem with my original solution was that
        # it skipped the last TWO values in the iteration not just the VERY LAST ONE
        
        return max(nums[0], nums[1])
