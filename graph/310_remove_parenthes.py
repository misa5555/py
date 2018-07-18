class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import defaultdict
        result = defaultdict(list)

        def dfs(st, count, opening, path):
            if opening < 0:
                return -1
            if not st:
                if opening == 0:
                    result[count].append(path)
                    return count
                else:
                    return -1

            min_count = len(s)
            if st[0] == '(':
                # use the first one
                use_first_count = dfs(st[1:], count, opening + 1, path + st[0])
                if use_first_count != -1:
                    min_count = min(min_count, use_first_count)
                # Not use(or SKIP) the first one
                not_use_first_count = dfs(st[1:], count, opening, path)
                if not_use_first_count != -1:
                    min_count = min(min_count, not_use_first_count)
            elif st[0] == ')':
                # use the first one
                use_first_count = dfs(st[1:], count, opening - 1, path + st[0])
                if use_first_count != -1:
                    min_count = min(min_count, use_first_count)
                # Not use(or SKIP) the first one
                not_use_first_count = dfs(st[1:], count + 1, opening, path)
                if not_use_first_count != -1:
                    min_count = min(min_count, not_use_first_count)
            else:
                min_count = dfs(st[1:], count, opening, path + st[0])
            return min_count

        _min = dfs(s, 0, 0, '')
        return (list(set(result[_min])))

s = Solution()
s.removeInvalidParentheses("(a)())()")