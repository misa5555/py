class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def check(n1, n2):
            flg1 = (n1 == 6 and n2 == 9) or (n1 == 9 and n2 == 6)
            flg2 = (n1 == n2) and (n1 in [0, 1, 8])
            return flg1 or flg2

        if len(num) == 1:
            return int(num[0]) in [0, 1, 8]
        mid = len(num) // 2
        for i in range(mid):
            left = int(num[i])
            right = int(num[-(i+1)])
            if not check(left, right):
                return False
        if len(num) % 2 == 0:
            return True
        else:
            return num[mid] in [0, 1, 8]
s = Solution()
print(s.isStrobogrammatic("69"))
