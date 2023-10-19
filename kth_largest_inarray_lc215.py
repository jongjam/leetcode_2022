class Solution:
    def findKthLargest(self, nums, k):
        # Guess it can just pull nums straight in ?
         # Getting the pivot at the end of the array
        
        # For simplicity changing K to get rid of any of that idx bulshit
        k = len(nums) - k
        # Left and right are start and end
        
        def quick_select(start, end) :
            # l and right are the bounds... don't try and remember just do wwhat you know
            # i is like j it will go up no matter what
            i = start
            pivot = end
            for j in range(start, end) : # stops before the pivot duh
                if nums[j] <= nums[pivot] :            
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
                    
          
            nums[i], nums[pivot] = nums[pivot], nums[i]
            pivot = i # The pivot location is now where i is
            # Updating this accordingly for ease of readability
            if pivot < k : # look to the right 
                return quick_select(pivot + 1, end)
            elif pivot > k : 
                return quick_select(start, pivot - 1)
            else :
                print(nums)
                return nums[pivot]
        
        return quick_select(0, len(nums) - 1)
    
def main() :
    nums = [3,2,1,5,6,4]
    k = 2
    print(Solution.findKthLargest(nums, k))
    print(nums)