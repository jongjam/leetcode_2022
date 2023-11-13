class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = {n:i for i, n in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []

        for i in nums2 :
            while stack and i > stack[-1] :
                idx = s.get(stack.pop())
                result[idx] = i

            
            if i in s.keys() :
                stack.append(i)


        return result
    
class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = dict()

        for i, a in enumerate(nums2) :
            s[a] = i
        
        print(s)
        result = [-1] * len(nums1)
        for i, n in enumerate(nums1) :
            j = s.get(n) + 1
            while j < len(nums2) :
                if nums2[j] > n :
                    result[i] = nums2[j]
                    break
                j += 1
            
         

        return result