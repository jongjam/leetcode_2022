class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Guess it can just pull nums straight in ?
         # Getting the pivot at the end of the array
        
        # For simplicity changing K to get rid of any of that idx bulshit
        k = len(nums) - k
        # Left and right are start and end
        
        def quick_select(start, end) :
            # l and right are the bounds... don't try and remember just do wwhat you know
            # i is like j it will go up no matter what
            p = start
            pivot = nums[end]
            for j in range(start, end) : # stops before the pivot duh
                if nums[j] <= pivot :            
                    nums[j], nums[p] = nums[p], nums[j]
                    p += 1
                
            nums[p], nums[end] = nums[end], nums[p]
             # The pivot location is now where i is
            # Updating this accordingly for ease of readability

            # P or I is where the pivot will end up by the end
            if p > k : 
                return quick_select(start, p - 1)
            elif p < k : # look to the right 
                return quick_select(p + 1, end)
            else :
                return nums[p]
        
        return quick_select(0, len(nums) - 1)