def searchRange(nums, target):
        l = 0
        r = len(nums) - 1
        
        # Did not know.... have to find them IN ORDER
        
        # Trying to find smallest index of target and largest index of target
        while l <= r :
            m = l + (r - l) // 2
           
            mval = nums[m]
            if mval > target :
                r = m - 1
            elif mval < target :
                l = m + 1
            else :
                res = [m, m]
                prev = m - 1
                next = m + 1
                
                if prev >= 0:
                    res[0] = find_max_upto_target(nums, 0, m, mval) # finds the first
                
                if next <= len(nums) - 1  :
                    res[1] = find_min_upto_target(nums, m, len(nums) - 1, mval) # finds the last
                
                return res
                # do binary search again 0 to mid (smaller)
                # do binary search again mid to end (bigger)
                # start = min(start, m)
                #     # how to update the bounds
                # end = max(end, m)

                # if we found another eight and 
        return [-1, -1]
    
def find_max_upto_target(nums, l, r, tar_max) :
    l = l
    r = r
    
    while l < r :
        m = l + (r - l) // 2
        
        if nums[m] == tar_max :
            r = m - 1
        else : #nums[m] != tar_max
            if l + 1 == r :
                break
            l = m
    
    return l + 1 # will need to return l + 1

def find_min_upto_target(nums, l, r, tar_max) :
    l = l
    r = r
    
    while l < r :
        m = l + (r - l) // 2
        
        if nums[m] == tar_max :
            l = m + 1
        else :
            r = m
    return r - 1 # will need to return r - 1
    
def main() :
    # nums = [1,2,3,4,5,6,6,8,8,8]
    # nums2 = [0,1,2,3,4,5,6,8,8,8]
    # nums3 = [8, 8, 8, 9, 9, 9, 10, 11, 12, 13, 14] # answer of this should be [3, 9]
    
    # nums4 = [1,4]
    # maxres = find_max_upto_target(nums4, 0, 1, 1)
    # minres = find_min_upto_target(nums3, 8)
    # print("max of left: ", maxres)
    # print("min of right: ", minres)
    
    
    nums = [5,7,7,8,8,10] 
    nums2 = [1, 1]
    target = 1
    
    print(searchRange(nums2, target))
main()

# Correct code for finding the first

# Finding the min value
#  while (i < j)
#     {
#         int mid = (i + j) /2; 
#         if (A[mid] < target) i = mid + 1; # moving left up to mid bc mid is smaller than target and trying to get closer
#         else j = mid; 
#     }
#     if (A[i]!=target) return ret;
#     else ret[0] = i;
        
    # Finding the max value        
#     // Search for the right one
#     j = n-1;  // We don't have to set i to 0 the second time.
#     while (i < j)
#     {
#         int mid = (i + j) /2 + 1;	// Make mid biased to the right
#         if (A[mid] > target) j = mid - 1;  
#         else i = mid;				// So that this won't make the search range stuck.
#     }
#     ret[1] = j;
#     return ret; 