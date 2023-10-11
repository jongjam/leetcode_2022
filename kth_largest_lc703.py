class KthLargest:

    def __init__(self, k, nums):
        first = [[k, nums]]
        print(first)
        first.append([10])
        print(first)

    # def add(self, val: int) -> int:
        

def main() :
    obj = KthLargest(3, [4, 5, 8, 2])
main()
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)