class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # s = "ABAB", k = 2 => 4
        from collections import defaultdict
        start = 0
        counter = defaultdict(int)
        max_count = 0
        result = 0
        for end in range(len(s)):
            counter[s[end]] += 1
            max_count = max(max_count, counter[s[end]])
            while end - start + 1 > k + max_count:
                counter[s[start]] -= 1
                start += 1

            result = max(result, end - start + 1)

        return result

s = Solution()
print(s.characterReplacement("AABABBA", 1))