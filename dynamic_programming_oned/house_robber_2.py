class Solution:
    def rob(self, nums: List[int]) -> int:
        # detect first and last........
        # i % len(nums)
        if len(nums) <= 1 :
            return nums[0]
        n = len(nums) - 1
        list_1 = nums[0:n]
        list_2 = nums[1:n+1]
        list_1.append(0)
        list_2.append(0)

        def bottom_up(nums) :
            for i in range(len(nums) - 3, -1, -1) :
                nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
            return max(nums[0], nums[1])

        return max(bottom_up(list_1), bottom_up(list_2))

