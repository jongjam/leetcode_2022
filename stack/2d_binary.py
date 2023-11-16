class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        # row no. is.... 5 / 4 = 1
        # box no. is 5 % 4 = 1

        l = 0
        r = (r * c) - 1

        while l <= r :
            mid = l + (r - l) // 2 # so now mid is like 5

            if matrix[mid // c][mid % c] < target :
                l = mid + 1
            elif matrix[mid // c][mid % c] > target :
                r = mid - 1
            else :
                return True
        
        return False