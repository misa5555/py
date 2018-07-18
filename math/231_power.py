class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = 1
        while tmp < n:

            tmp <<= 1
        return tmp == n
s = Solution()
print(s.isPowerOfTwo(4))
print(s.isPowerOfTwo(5))
