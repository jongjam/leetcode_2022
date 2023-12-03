def search(nums, target) :
    l = 0
    r = len(nums) - 1

    while l <= r :
        m = l + (r-l) // 2

        # we want to always look at the sorted half to look for target bc WE KNOW ascending order

        if nums[m] == target :
            return m
        
        if nums[l] <= nums[m] :
            if nums[l] <= target < nums[m] :
                r = m - 1
            else :
                l = m + 1
        else : # the right half is sorted
            if nums[m] < target <= nums[r] :
                l = m + 1
            else :
                r = m - 1

    return -1

def main() :
    nums = [5, 1, 3]
    target = 3
    print(search(nums, target))

main()
    