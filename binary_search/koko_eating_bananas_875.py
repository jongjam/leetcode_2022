class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        end = max(piles) # 11

        # So starting from 1 going up to... the max amo

        # so reverse engineering using the answer       
        time_exceeded = False


        for k in range(1, end) :     
            time = 0
            copy = list(piles)

            for pile in piles : 
                hours_taken = pile / k 
                hours_taken = math.ceil(hours_taken)
                
                time += hours_taken
            
                if time > h :
                    time_exceeded = True
                    break

            if not time_exceeded:
                return k
            time_exceeded = False
        
        return end
                
                
               

            
            
            


