class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def compose(pairs, mid):
            ans = []
            for pair in pairs:
                ans.append(pair[0] + mid + pair[1])
            return ans

        def helper(n):
            if n == 1:
                return ["0", "1", "8"]
            elif n == 2:
                return ["00", "11","69","88","96"]

            previous_ans = helper(n-2)
            pairs = ["00", "11","69","88","96"]
            ans = []
            for mid in previous_ans:
                for pair in pairs:
                    ans.append(pair[0] + mid + pair[1])
            return ans
        tmp_ans = helper(n)
        ans = []
        for el in tmp_ans:
            if el[0] == '0' and len(el) > 1:
                continue
            ans.append(el)
        return ans
s = Solution()
print(s.findStrobogrammatic(2))
print(s.findStrobogrammatic(3))
