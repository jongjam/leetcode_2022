class Solution:
    # basically just shoving every possibility in the decision tree into the result.        

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        perm = []
        # so choosing to add yourself before you go down or after basically
        def bt():
            if len(perm) == len(nums) :
                result.append(perm.copy())
                return 
            # maybe need liek a left and right thing
            for i in range(len(nums)) :
                if nums[i] not in perm :
                    perm.append(nums[i])
                    bt()
                    perm.pop()

        bt()
        return result
