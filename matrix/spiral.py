"""
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
"""
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def _print(dire, start, times):
            path = []
            crt = start
            for i in range(times):
                print(matrix[crt[0]][crt[1]])
                path.append(matrix[crt[0]][crt[1]])
                if dire == "right":
                    crt = (crt[0], crt[1]+1)
                elif dire == "down":
                    crt = (crt[0] + 1, crt[1])
                elif dire == "left":
                    crt = (crt[0], crt[1] - 1)
                else:
                    crt = (crt[0] - 1, crt[1])
            return path
        width = len(matrix[0])
        height = len(matrix)
        start = (0,0)
        ans = []
        while width >= 1 and height >= 1:
            if width == 1 and height == 1:
                ans.append(matrix[start[0]][start[1]])
                break
            elif width == 1:
                ans += _print("down", start, height)
                break
            elif height == 1:
                ans += _print("right", start, width)
                break

            ans += _print("right", start, width - 1)
            ans += _print("down", (start[0], start[1] + width - 1), height - 1)
            ans += _print("left", (start[0] + height - 1, start[1] + width - 1), width-1)
            ans += _print("up", (start[0] + height-1, start[1]), height-1)
            start = (start[0] + 1, start[1] + 1)
            width -= 2
            height -= 2
        return ans
s = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
s.spiralOrder(matrix)
