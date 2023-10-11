import heapq
class KthLargest:
    
    # Stream is the stream of integers, with k and nums in the requested format
    # k is the kth largest element to be referenced in the add function
    
    # The stream doesn't have to be in this format... just the result needs to be correct so I can use a heap without issue
    def __init__(self, k, nums):
        # for i, s in enumerate(nums):
        #     nums[i] = -s
            
        self.stream = nums
        self.k = k
        
        heapq.heapify(self.stream)
        
        while len(self.stream) > self.k :
            heapq.heappop(self.stream)
    
    # The add function adds a new value to the stream, and then returns the kth largest element
    
    def add(self, val) -> int:
        heapq.heappush(self.stream, val)
        
        while len(self.stream) > self.k :
            heapq.heappop(self.stream)
            
        return self.stream[0]
    
    def get_stream(self) :
        print(self.stream)

def main() :
    obj = KthLargest(3, [4, 5, 8, 2])
    result = obj.add(3)
    print("result of add:", result)
    result = obj.add(5)
    print("result of add:", result)
    obj.get_stream()
main()
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)