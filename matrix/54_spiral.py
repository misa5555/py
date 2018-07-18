class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        result += matrix.pop(0)
        while len(matrix) >= 1:
            matrix = list(zip(*matrix))[::-1]
            result += matrix.pop(0)

        print(result)

s =Solution()
matrix= [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
s.spiralOrder(matrix)