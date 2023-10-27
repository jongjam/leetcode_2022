import heapq


class Solution:
    def leastInterval(self, tasks, n):
        # N shows the amount of space where two chars cannot be repeated
        # So I was right in using a counter
        time = 0
        hp = []
        q = [] # use append and pop(0) to use like a queue
        # So count all the elements up, which I was thinking
        if n == 0 :
            return len(tasks)
        
        # Get counts of all elements
        count = {}
        
        for i in tasks :
            if i not in count :
                count[i] = 1
            else :
                count[i] += 1
        # If all on cooldown need to idle
        # We want to get rid of the more frequent characters first...
        keys = count.keys()
        for c in keys :
            nums = count[c]
            heapq.heappush(hp,-nums) # Used a maxheap

      
        # The basic logic here... will continue as heap not empty
        while len(hp) != 0 :
            element = 1 + heapq.heappop(hp)
            time += 1 
            if element != 0 :
                # current task will be available at this next time
                time += n
                q.append((element, time))

            cur_time = q[0][1]
            cur_ele = q[0][0]
            
            if cur_time == time :
                q.pop(0)
                heapq.heappush(hp, cur_ele)


        return time
    
def main():
    ob = Solution()
    tasks = ["A","A","A","B","B","B"] 
    n = 2
    print(ob.leastInterval(tasks, n))
    