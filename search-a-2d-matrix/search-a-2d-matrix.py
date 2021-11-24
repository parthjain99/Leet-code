class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m=len(matrix[0])
#         n=len(matrix)
#         for i in range(n):
#             if matrix[i][m-1]<target:
#                 continue
#             for j in range(m):
                
#                 if matrix[i][j]==target:
#                     return True
#         return False
        if not matrix or not matrix[0]: return False
        m, n = len(matrix[0]), len(matrix)
        beg, end = 0, m*n - 1
        while beg < end:
            mid = (beg + end)//2
            if matrix[mid//m][mid%m] < target:
                beg = mid + 1
            else:
                end = mid
        return matrix[beg//m][beg%m] == target
