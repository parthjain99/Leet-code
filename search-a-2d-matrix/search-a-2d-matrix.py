class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix[0])
        n=len(matrix)
        for i in range(n):
            if matrix[i][m-1]<target:
                continue
            for j in range(m):
                
                if matrix[i][j]==target:
                    return True
        return False

