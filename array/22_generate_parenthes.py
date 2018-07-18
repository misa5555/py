class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        tmp = {'(': 1}
        result = []

        for i in range(2 * n - 1):
            new_tmp = {}
            for k, v in tmp.items():
                if v > 0:
                    new_tmp[k + ')'] = v - 1
                if v < n:
                    new_tmp[k + '('] = v + 1
            tmp = new_tmp

        for k, v in tmp.items():
            if v == 0:
                result.append(k)
        print(tmp)
        print(result)
        return result

s = Solution()
s.generateParenthesis(3)