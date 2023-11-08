class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0

        # I'm guessing you want to look at the whole thing and only keep the max
        while l < r :
            x = r - l
            y = min(height[l], height[r])
            area = max(x * y, area)
           

            if height[l] > height[r] :
                r -= 1
            elif height[l] <= height[r] : # What to do if equal ?
                l += 1


        return area