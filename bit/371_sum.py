class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == b:
            return 2 * a

        larger = bin(max(a, b))
        smaller = bin(min(a, b))
        carry = 0
        diff = len(larger) - len(smaller)
        s = f"0b{'0' * diff}{bin(min(a, b))[2:]}"

        i = len(larger) - 1
        result = ''
        while i != 'b':
            if larger[i] + smaller[i] + carry > :
                carry = 1
                result = '0' + result
