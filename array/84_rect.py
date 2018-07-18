class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        area, max_area = 0, 0
        def popping(stack, i, max_area):
            top = stack.pop()
            rect = heights[top] * (i - top)
            return max(max_area, rect)

        for i in range(len(heights)):
            if not stack or (stack and heights[stack[-1]] < heights[i]):
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    max_area = popping(stack, i, max_area)
                stack.append(i)

        while stack:
            max_area = popping(stack, len(heights), max_area)

        print(max_area)
        return max_area

s = Solution()
# s.largestRectangleArea([2,1,5,6,2,3])
s.largestRectangleArea([2,1,2])