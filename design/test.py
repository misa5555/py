def get_shortest_unique_substring(arr, str):
    '''
    ans = ''
    minLen = len(str)
    for i in range(len(str)):
      for j in range(i, len(str)):
        if len(set(str[i:j+1]) & set(arr)) == len(arr):
          if minLen > j - i:
            ans = str[i:j+1]
            minLen = j - i
    return ans
    '''

    # square O (n^2), space O(1)

    # arr = ['x','y','z'], str = "xyyzyzyx"
    #                             |  |

    # counter = {'x': 1, 'y':2, z: 1 }
    # ["A","B","C"], "ADOBECODEBANCDDD"
    #                  |       |

    from collections import Counter
    counter = Counter()
    total = 0
    i = 0
    minLen = len(str)
    ans = ''
    for j in range(len(str)):
        if str[j] in arr:
            # print(counter.get(str[j]))
            if not counter.get(str[j]) or counter.get(str[j]) == 0:
                total += 1
            counter[str[j]] += 1
        if total == len(arr):
            while not counter.get(str[i]) or counter[str[i]] > 1:
                if counter.get(str[i]):
                    counter[str[i]] -= 1
                i += 1
            if j - i < minLen:
                minLen = j - i + 1
                ans = str[i:j + 1]

        return ans
