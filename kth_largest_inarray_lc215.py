class Solution:
    # Quick sort.... can use sort python thingy but no one will just
    # let that shit slide GOD FUCKING DAMNIT!
    og_len = 0
    idx = 0
    
    def partition(self, nums, start, end) :
        i = start - 1 # I is the location of the larger element and will only go up if j passes over a larger item
        j = start

        pivot = end

        while j < end :
            if nums[j] < nums[pivot] :
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
        
        i += 1
        nums[i], nums[pivot] = nums[pivot], nums[i]

        return i # I is the location of the old pivot and partitions will continue based on this location


    def quick_select(self, nums, start, end, k) : 
        if end <= start :
            print('help')
            return nums[self.idx]
        self.partition(nums, start, end) # Problem I don't use pivot
        half = self.og_len // 2

        if k < half :
            self.quick_select(nums, self.idx + 1, end, k)
        elif k > half :
            self.quick_select(nums, start, self.idx - 1, k)
        else :
            print('gotcha bitch')
            return nums[self.idx]

    def findKthLargest(self) -> int:
        # It is quick sort except the next partion will happen
            # if k less than half nums length... start length - k to end
            # if k greater than half nums length... start 0 to length - k
        nums = [2, 4, 1, 3]
        k = 2
        
        self.idx = len(nums) - k
        self.og_len = len(nums)
        self.quick_select(nums, 0, len(nums) - 1, k)
    

   