import heapq

# Use numpy to make it... reversed
# You could sort it and do it... duh        
# Use of a max heap cut down to K size so head is kth largest element
# def findKthLargest(nums, k) :
#     heap = []
#     # When working with a list to have it in sorted order... you must add in a stream 
#     for i in nums :
#         heapq.heappush(heap, i)
    
#     while len(heap) > k :
#         heapq.heappop(heap)
#     return heapq.heappop(heap)

# Max heap
def findKthLargest(nums, k) :
    heapq._heapify_max(nums)
    print(nums)
    i = 0
    while i < 2:
        heapq.heappop(nums)
        i += 1
    return heapq.heappop(nums)

def main() :
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    # Should print 5 because second largest is 5
    print(findKthLargest(nums, k))

main()    
