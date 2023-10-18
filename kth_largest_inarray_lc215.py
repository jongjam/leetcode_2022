class Solution:
    # Quick sort.... can use sort python thingy but no one will just
    # let that shit slide GOD FUCKING DAMNIT!
    og_len = 0
    idx = 0

    def quick_select(self, nums, start, end, k) : 
        if end <= start :
            return nums[self.idx]
        pivot = partition(nums, start, end)
        half = self.og_len // 2

        if k < half :
            quick_select(nums, self.idx, end, k)
        if k >= half :
            quick_select(nums, start, self.idx, k)

    def partition(self, nums, start, end) :
        i = start - 1 # I is the location of the larger element and will only go up if j passes over a larger item
        j = start

        pivot = end

        while j <= end :
            if nums[j] < nums[pivot] :
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
        
        i += 1
        nums[i], nums[pivot] = nums[pivot], nums[i]

        return i # I is the location of the old pivot and partitions will continue based on this location



    def findKthLargest(self, nums: List[int], k: int) -> int:
        # It is quick sort except the next partion will happen
            # if k less than half nums length... start length - k to end
            # if k greater than half nums length... start 0 to length - k
        self.idx = len(nums) - k
        self.og_len = len(nums)
        return quick_select(nums, 0, len(nums) - 1, k)

   