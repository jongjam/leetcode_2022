def productExceptSelf(nums):
        
        # Cannot use division 
        # Runs in O(n) time so I have to go through with one pass
        left = [1] * len(nums)# Product on left
        right = [1] * len(nums)# Product on right

        

        for i in range(len(nums)) :
            l_prod = 1
            r_prod = 1
            l = i - 1
            r = i + 1

            while l >= 0 :
                l_prod = l_prod * nums[l]
                l -= 1
            while r < len(nums) :    
                r_prod = r_prod * nums[r]
                r += 1
            left[i] = l_prod
            right[i] = r_prod
        
        result = [left[i] * right[i] for i in range(len(right))]
        return result
    
def main():
    
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
    
main()