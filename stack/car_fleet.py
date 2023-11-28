class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      
        cars = [[p,s] for p,s in zip(position,speed)]
        cars.sort()
        
        count = 0
        # while stack and temp > nums[stack[-1]]: # just put the indexes to get temps
        #         idx = stack.pop()
        #         answer[idx] = i - idx

        #     stack.append(i)

        # if a certain thing matches the criteria (bigger or smaller) keep popping
        # at the end add yourself to STACK !
        cur_slow_max = 0
        for i in range(len(cars) - 1, -1, -1) :
            time_to_target = (float(target) - cars[i][0]) / cars[i][1]
            if time_to_target > cur_slow_max :
                count += 1
                cur_slow_max = time_to_target
 
        return count