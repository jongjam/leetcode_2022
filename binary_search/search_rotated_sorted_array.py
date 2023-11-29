class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r :
            mid = l + (r - l) // 2

            if nums[mid] > nums[r] :
                l = mid + 1
            else : # nums[mid] <= nums[r]
                r = mid

        pivot = l # idx location of pivot (the minimum) is found 
        
        while l <= r :
            mid = l + (r - l) // 2
            real_mid = (mid + pivot) % len(nums)

            if nums[real_mid] < target :
                l = real_mid + 1
            elif nums[real_mid] > target :
                r = real_mid - 1
            else :
                return real_mid

        return -1