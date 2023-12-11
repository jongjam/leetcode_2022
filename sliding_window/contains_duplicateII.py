class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # find the two indices that equal each other and the difference between the indecies for them is less than k
        # find the duplicate pair within window of size k 

        nums_in_wd = set() # nums in window
        count = 0   
        l = 0

        for r in range(len(nums)) :
            if r > k :
                nums_in_wd.remove(nums[l]) # nums in window
                l += 1
            if nums[r] not in nums_in_wd :
                nums_in_wd.add(nums[r]) # adding cur num and idx to map
            elif nums[r] in nums_in_wd :
                return True
            count += 1
        
        return False
