def countSmallerToTheRight(nums):
    # [3, 8, 4, 1]
    ans = [0] * len(nums)

    def sort(enum):
        if not enum or len(enum) == 1:
            return enum
        mid = len(enum) // 2
        left, right = sort(enum[:mid]), sort(enum[mid:])
        l, r = 0, 0

        while l < len(left) and r < len(right):
            if left[l][1] <= right[r][1]:
                ans[left[l][0]] += r
                enum[l+r] = left[l]
                l += 1
            else:
                print((l, r ))
                enum[l+r] = right[r]
                r += 1
        while r < len(right):
            enum[l+r] = right[r]
            r += 1
        while l < len(left):
            ans[left[l][0]] += r
            enum[l + r] = left[l]
            l += 1


        return enum
    enum = list(enumerate(nums))
    sort(enum)
    print(ans)
    return ans
countSmallerToTheRight([5,2,6,1])



