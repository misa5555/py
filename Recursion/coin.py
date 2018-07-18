class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('Inf')
        dp = [0] + [MAX] * amount
        def helper(coins, amount):
            if amount == 0:
                return 0

            for i in range(1, amount + 1):
                dp[i] = min([dp[i-c] if i-c >= 0 else MAX for c in coins])

            return [dp[amount], -1][dp[amount] == MAX]
        coins.sort()

        result = helper(coins, amount)

        print(dict((key,value) for key, value in dp.items() if value != -1))
        print(result)
        return result
s = Solution()
# s.coinChange([1, 2, 5], 11)
#
# s.coinChange([3,2], 1)
# s.coinChange([2], 3)
# s.coinChange([3,7,405,436], 8839) # 25
# s.coinChange([186,419,83,408], 6249) # 20
s.coinChange([208,170,205,425,124,375], 7130) #18
s.coinChange([208,170,205,425,124,375], 785) #18
