#https://codefights.com/interview-practice/task/izLStwkDr5sMS9CEm
def findLongestSubarrayBySum(s, arr):
    total = 0
    sums = {}
    ans = [0, -1]
    for i in range(len(arr)):
        total += arr[i]
        tmp = [i, i]
        if total - s in sums:
            tmp = [sums[total - s] + 2, i + 1]
        if total - s == 0:
            tmp = [1, i + 1]
        if tmp[1] - tmp[0] > ans[1] - ans[0]:
            ans = tmp
        sums[total] = i
    if ans[0] == 0:
        return [-1]
    return ans
findLongestSubarrayBySum(0, [1, 0, 2])
# findLongestSubarrayBySum(3, [0, 3, 0])