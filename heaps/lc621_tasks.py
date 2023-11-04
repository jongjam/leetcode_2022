from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks, n):
        # N shows the amount of space where two chars cannot be repeated
        # So I was right in using a counter
        time = 0
        counts = Counter(tasks)
        maxHeap = [-x for x in counts.values()]
        heapq.heapify(maxHeap)

        q = deque()

        # The basic logic here... will continue as heap not empty
        while maxHeap or q: # As long as they are not length 0
            time += 1 
            if maxHeap :
                element = 1 + heapq.heappop(maxHeap)
                if element : # is not 0
                    # current task will be available at this next time
                    next_ready_time = time + n
                    q.append([element, next_ready_time])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
    
def main():
    ob = Solution()
    tasks = ["A","A","A","B","B","B"] 
    n = 2
    result = ob.leastInterval(tasks, n)
    