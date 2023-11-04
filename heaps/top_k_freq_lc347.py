from collections import Counter

def topKFrequent(nums, k):
        result = [0] * k
        counts = Counter(nums) # Quick way to get counts of everything and put in map
        buckets = [[] for i in range(len(nums) + 1)]

        for num in counts.keys() :
            count = counts[num]
            buckets[count].append(num) 

        stopper = 0
        for i in range(len(buckets) - 1, 0, -1) :
            if stopper >= k :
                return result
            for j in buckets[i] : # Should skip over empty ones
                result[stopper] = j
                stopper += 1

        # Uses a reverse bucket sort method
        # Keys are the count and values are the number
        # Count cannot exceed the length of nums

        # Using a heap just create a key pair of count and the element
        # Return tuple[1] for tuple in list 
        # This is easy and an O(n log n) with heap


        return result
            
def main() :
    nums = [1,1,1,2,2,3] 
    k = 2
    topKFrequent(nums, k)
    
main()