class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sorting the list first for binary search
        result = []
        visited = set()
   
        for i, a in enumerate(nums) :
            if i > 0 and a == nums[i - 1] :
                continue
            
            tar = nums[i] * -1 # let's say -1 in this case
            l = i + 1
            r = len(nums) - 1

            while l < r :
                if nums[l] + nums[r] > tar :
                    r -= 1
                elif nums[l] + nums[r] < tar :
                    l +=1
                else :
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r :
                        l += 1
                
     
        return result