# https://codefights.com/interview-practice/task/5vXzdE9yzjsoMZ9sk
def swapLexOrder(str, pairs):
    parent = [-1] * len(str)

    def swap(s, ary):
        ls = list(s)
        partial = [s[idx] for idx in ary]
        for i, el in enumerate(sorted(partial, reverse=True)):
            ls[ary[i]] = el
        return ''.join(ls)

    def find_parent(n):
        print(n)
        if parent[n] != -1:
            return find_parent(parent[n])
        else:
            return n

    def union(n, m):
        p1 = find_parent(n)
        p2 = find_parent(m)
        if p1 != p2:
            parent[min(p1, p2)] = max(p1, p2)

    for p in pairs:
        union(p[0] - 1, p[1] - 1)

    from collections import defaultdict
    groups = defaultdict(list)
    for i in range(len(parent)):
        p = find_parent(parent[i])
        if p == -1:
            groups[i].append(i)
        else:
            groups[p].append(i)

    for k, v in groups.items():
        if len(v) > 1:
            str = swap(str, v)
    return str


s1 = "abdc"
p1 =  [[1,4],
 [3,4]]
# print(swapLexOrder(s1, p1))

s2 = "abcdefgh"
p2 = [[1,4],
 [7,8]]
# print(swapLexOrder(s2, p2))
s3 = "acxrabdz"
p3 = [[1,3],
 [6,8],
 [3,8],
 [2,7]]
# print(swapLexOrder(s3, p3))

s4 = "qvspxdrbvwfuaahtzbpjudfyzccgzwynkgihwmdshvfnvyvfjc"
p4 = [[16,26],
 [2,25],
 [25,27],
 [19,20],
 [13,20],
 [4,26],
 [19,27],
 [18,26],
 [13,23],
 [1,4],
 [11,19],
 [16,19],
 [25,28],
 [19,30],
 [19,25],
 [1,11],
 [2,20],
 [10,22],
 [6,19],
 [7,26],
 [3,30],
 [15,23],
 [12,26],
 [1,3],
 [3,12],
 [3,26],
 [16,30],
 [2,16],
 [4,13]]
print(swapLexOrder(s4, p4))
# zwvuxtsbvwrqpapjzhgfudfydccbzaynkgihwmdshvfnvyvfjc
# zwvuxtsbvwrqpapjzhgfudfydccbzaynkgihwmdshvfnvyvfjc