class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        end = max(piles) # 11
        # So starting from 1 going up to... the max amo

        # so reverse engineering using the answer       
        time_exceeded = False
        l = 1
        r = end
        while l < r :
            mid = l + (r - l) // 2
            time = self.calculate_time(mid, piles)
            print("m: ",mid)
            print("t: ",time)
            if time <= h : # it's too fast
                r = mid
            elif time > h : # it's too slow
                l = mid + 1

        return l

        # ok so if you're too fast... follow the templates...
                
    def calculate_time(self, k, piles) :
        time = 0

        for pile in piles : 
            hours_taken = pile / k 
            hours_taken = math.ceil(hours_taken)
            time += hours_taken
        return time
               

            
            
            


