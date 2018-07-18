def combinationSum(a, sum):
    dp = {0: [[]]}
    result = []

    def helper(arr, target):
        if target == 0:
            return [[]]
        if arr[0] > target or target < 0:
            return False
        if dp.get(target):
            return dp.get(target)

        ans = []
        for i in range(len(arr)):
            tmp = helper(arr, target - arr[i])
            if tmp != False:
                print(tmp)
                ans += [tuple(list(t) + [arr[i]]) for t in tmp]
        dp[target] = list(set(sorted(ans)))
        return list(set(sorted(ans)))

    return helper(a, sum)
combinationSum([2,3,5,9], 9)