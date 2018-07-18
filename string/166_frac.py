class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = ""
        if denominator * numerator < 0:
            sign = "-"
            denominator, numerator = abs(denominator), abs(numerator)

        int_part, dic_part = 0, ""

        int_part = numerator // denominator
        if numerator % denominator == 0:
            return sign + str(int_part)

        remainder = numerator - int_part * denominator
        from collections import defaultdict
        rem_past = []
        # check if there is cycle in dic_part
        while not remainder in rem_past:
            rem_past.append(remainder)
            remainder *= 10
            tmp_quotient = remainder // denominator
            remainder = remainder - tmp_quotient * denominator
            dic_part += str(tmp_quotient)
            if remainder == 0:
                return sign + str(int_part) + "." + str(dic_part)

        # stt = rem_past[remainder]
        idx = rem_past.index(remainder)
        s = dic_part[0:idx] + "(" + dic_part[idx:] + ")"

        return sign + str(int_part) + "." + s

s = Solution()
s.fractionToDecimal(-50, 8)