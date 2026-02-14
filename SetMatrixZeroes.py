class Solution(object):
    def setZeroes(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    for c in range(cols):
                        if matrix[i][c]!=0:
                            matrix[i][c]=-1
                    for r in range(rows):
                        if matrix[r][j]!=0:
                            matrix[r][j]=-1
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==-1:
                    matrix[i][j]=0
