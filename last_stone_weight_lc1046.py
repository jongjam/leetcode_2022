# Stones is an array of ints
from heapq import _heapify_max, _heappop_max, heappush


def lastStoneWeight(stones) :
    # Creating a heap of 
    build_max_heap(stones)
    
    i = 0
    while len(stones) >= 2 :
        
       
        y = _heappop_max(stones)
        x = _heappop_max(stones)
         
        new = abs(y - x)
        if new != 0 :
            heappush(stones, new)
            _heapify_max(stones)
            
        print('We combine ', x , 'and ', y, 'to get ', new, 'so the array converts to ',stones)
        i += 1    
    
def build_max_heap(stones) :
    n = len(stones)
        
    for i in range(n // 2, 0, -1) :
        _heapify_max(stones)
    
def main() :
    stones = [2,7,4,1,8,1,1]
    lastStoneWeight(stones)

main()