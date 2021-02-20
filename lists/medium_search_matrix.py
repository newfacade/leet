from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        编写一个高效的算法来搜索升序 m x n 矩阵 matrix 中的一个目标值 target
        从右上角向左下角搜索即可，因为n和m都大于1，因此无需特判
        """
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
