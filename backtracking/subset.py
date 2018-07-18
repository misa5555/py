def sumSubsets(arr, num):

    def helper(arr, num):
        if num == 0:
            return [[]]
        if not arr or arr[0] > num or num < 0:
            return -1
        result = []
        for i, n in enumerate(arr):
            if arr[i] == arr[i-1]:
                continue
            tmp = helper(arr[i + 1:], num - arr[i])
            if tmp != -1:
                result += [[arr[i]] + t for t in tmp]
        return list(result)

    return helper(arr, num)


def classifyStrings(s):
    vowels = set(["a", "e", "i", "o", "u"])
    state = 'good'
    v_repeat, s_repeat = 0, 0
    v_repeat_max, s_repeat_max = 0, 0
    for i in range(len(s)):
        if s[i] == '?':
            v_repeat += 1
            s_repeat += 1
        elif s[i] in vowels:
            v_repeat += 1
            s_repeat = 0
        else:
            v_repeat = 0
            s_repeat += 1
        s_repeat_max = max(s_repeat_max, s_repeat)
        v_repeat_max = max(v_repeat_max, v_repeat)
    if s_repeat_max >= 5 and v_repeat_max >= 3:
        return 'bad'
    elif s_repeat_max >= 5 or v_repeat_max >= 3:
        return 'mix'
    else:
        return 'good'

print(classifyStrings("aa?bbbb"))
print(classifyStrings("aa?bbb?a?bbb?aa"))
# print(sumSubsets([4], 4))
# print(sumSubsets([1,2,3,4,5], 5))
# print(sumSubsets([1, 2, 2, 3, 4, 5], 5))