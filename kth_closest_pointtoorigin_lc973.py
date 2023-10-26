import math
import heapq
# [[1,3],[-2,2]], k = 1 returns [-2, 2]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        # Calculate points distance to 0
        def distance(point) :
            x = point[0]
            y = point[1]

            dist = math.sqrt(x**2 + y**2)
            return dist
            
        # Heap of points and distance to 0,0
        hp = []
        
        # Using a max heap and polling all the bigger items leaves us with
        # a heap sized perfectly for our answer
        for i in range(len(points)) :
            dist = distance(points[i])
            heapq.heappush(hp, (-dist, points[i]))
            if len(hp) > k :
                heapq.heappop(hp)
        
        return [tuple[1] for tuple in hp]

def main() :
    points = [[1,3],[-2,2]]
    obj = Solution()
    result = obj.kClosest(points, 1)
    print(result)

main()