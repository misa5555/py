class Solution:
    def _trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        #return 6.
        def calcWater(i, j, stack):
            ceiling = min(height[i], height[j])
            sum = 0
            while stack:
                amount = ceiling - stack.pop()
                if amount > 0: sum += amount
            return sum


        i = 0
        stack = []
        result = 0
        while i < len(height) - 1:
            if height[i] == 0:
                i += 1
                continue
            j = i + 1
            found = False
            while j < len(height):
                stack.append(height[j])
                if height[j] >= height[i]:
                    found = True
                    result += calcWater(i, j, stack)
                    i = j
                    break
                j += 1
            if not found:
                i += 1
                stack = []

        print(result)
        return result

    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        result = 0
        while right >= left:
            if height[right] >= height[left]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1
        print(result)
        return result



s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
s .trap([4,2,3])