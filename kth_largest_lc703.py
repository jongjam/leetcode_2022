class KthLargest:
    def __init__(self, k, nums):
        self.stream = [[k, nums]]

    def add(self, val) -> int:
        self.stream.append([val])
    
    def get_stream(self) :
        print(self.stream)

def main() :
    obj = KthLargest(3, [4, 5, 8, 2])
    obj.add(10)
    obj.get_stream()
main()
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)