class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
    
    
        # in sequence nums[i - 1] < nums[i] < nums[i + 1] : right = mid - 1 go left
        # out of sequence nums[i - 1] > nums[i] > nums[i + 1] : left = mid + 1 go right
        # if nums[i - 1] > nums[i] and nums[i + 1] > nums[i] return mid
        while l < r :
            mid = l + (r - l) // 2

            if nums[mid] > nums[r] : # mid is not in the sorted section and the smaller nums are to the right of us
                l = mid + 1
            else : # we are currently in the sorted section so the min is to the left of us
                r = mid 
            
         # at this point, left and right converge to a single index (for minimum value) since
        # our if/else forces the bounds of left/right to shrink each iteration:

        # when left bound increases, it does not disqualify a value
        # that could be smaller than something else (we know nums[mid] > nums[right],
        # so nums[right] wins and we ignore mid and everything to the left of mid).

        # when right bound decreases, it also does not disqualify a
        # value that could be smaller than something else (we know nums[mid] <= nums[right],
        # so nums[mid] wins and we keep it for now).

        # so we shrink the left/right bounds to one value,
        # without ever disqualifying a possible minimum

        return nums[l]