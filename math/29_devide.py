class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_positive = dividend * divisor
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            print(f"dividend:{dividend}")
            tmp = divisor
            while dividend >= (tmp << 1):
                print(f"tmp:{tmp}")
                tmp <<= 1
            dividend -= tmp
            ans += tmp // divisor
        return ans

s = Solution()
print(s.divide(15, 3))
