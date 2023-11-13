class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        # so this can be done in brute force pretty easily 

        answer = [0] * len(nums)
        stack = []

   
        
        # i has to be greater than idx
        for i, temp in enumerate(nums) :
            while stack and temp > nums[stack[-1]]: # just put the indexes to get temps
                idx = stack.pop()
                answer[idx] = i - idx

            stack.append(i)
            

        return answer 
                
    