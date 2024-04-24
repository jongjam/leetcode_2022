class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # if we look at this from bottom up, 
        # the very end will always be just 1 if we have an increasing thing
        # will need another data source bc can't overwrite if doing bottom up 
        # it's not consectuive are you fucking kidding me
        dp = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1) :
            dp[i] = dp[i] + dp[i + 1] if nums[i] > nums[i + 1] else dp[i + 1]
            
        return dp[0]
