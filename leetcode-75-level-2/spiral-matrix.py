
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        output.extend(matrix[0])
        matrix.pop(0)
        while matrix:
            matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0])-1, -1, -1)]
            output.extend(matrix.pop(0))
        return output

