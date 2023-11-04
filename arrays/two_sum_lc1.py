class Solution:
    # use of the maps and adding the things together
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        # num pairs, key is the num, the value is the counterpart to get to the target(target - key)
        # target - key is the key, nums is the value
        for i in range(len(nums)) :
            if target - nums[i] in sums :
                return [i, sums[target - nums[i]]]
            else :
                sums[nums[i]] = i