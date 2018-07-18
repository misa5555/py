dp = [0] * 238
def helper(nums, target):
    if target == 0:
        return 1
    if not nums:
        return 0
    if dp[target] > 0:
        return dp[target]
    if nums[0] > target:
        return -1
    ans = 0
    for i, n in enumerate(nums):
        new_nums = nums[i+1:]
        if target - n >= 0:
            tmp = helper(new_nums, target - n)
            if tmp > 0:
                ans += tmp
    dp[target] = ans
    return ans



def str237(str):
    arr = []
    for ch in list(str):
        arr.append(ord(ch))

    arr.sort()


    helper(arr, 237)
    print(dp[-1])
str237('vw')
str237("Hello world!")
str237("Hello world!!")
