class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def binary_search(ary, target):

            lo, hi = 0, len(ary) - 1
            while lo <= hi:
                mid = lo + hi // 2
                if ary[mid] == target:
                    return True
                elif ary[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False

        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n - 1]:
                if binary_search(matrix[i], target):
                    return True
            elif matrix[i][0] > target:
                return False

        return False
s = Solution()
ary = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(s.searchMatrix(ary, 5))