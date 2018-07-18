class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

        Input: 1994
        Output: "MCMXCIV"
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
        """
        dividors = [1000, 500, 100, 50, 10, 5, 1]
        lst = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        ans = ''

        i = 0
        while num > 0:
            if dividors[i] > num:
                i += 1
                continue
            if (str(num)[0] == '9') and 1 <= i <= len(dividors) - 2:
                ans += lst[dividors[i + 1]] + lst[dividors[i - 1]]
                num %= dividors[i+1] * 9
                i += 1
                continue
            if str(num)[0] == '4' and i >= 1:
                ans += lst[dividors[i]] + lst[dividors[i-1]]
                num %= 4 * dividors[i]
                i += 1
                continue

            ch = lst[dividors[i]]
            ans += ch * (num // dividors[i])
            num %= dividors[i]
            i += 1

        return ans
s = Solution()
# s.intToRoman(58)
print(s.intToRoman(1994))


