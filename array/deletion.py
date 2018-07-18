def deletion_distance(str1, str2):
    # pass # your code goes here
    # dog => frog
    # 'e' 'a' => 2
    # 'e', 'e' => 0
    # 'dog', '' => len(str1)
    # 'dog', 'd' => 'og', '' => 2
    # 'heat', 'hit' => 'eat', 'it' => 'ea', 'i'

    if str1 == str2:
        return 0
    # check if two strings have common character
    # 'og' and 'frog' => 2
    # 'd' 2 + 1
    # 'f' 2

    dp = [[-1 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    # str1[0], str2[0]
    # "" and ""
    dp[0][0] = 0

    # dog frog -> (og, frog), (dog, rog)
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1

    return dp[-1][-1]


''' 
os
so

Case 1: The last character in str1 is equal to the last character in str2. In that case, one may assume that these two characters aren’t deleted, and look at the prefixes that don’t include the last character.

Case 2: The last character in str1 is different from the last character in str2. In that case, at least one of the characters must be deleted, thus we get the following equation: d(str1,str2) = 1 + min( d(str1.substring(0, n-1), str2), d(str1, str2.substring(0, m-1)) ) where n is the length of str1, m is the length of str2, and d(x,y) is the deletion distance between x and y.

dp(i,j) = current + min(dp[i-1, j], dp[i, j-1])

O(max(len(str1), len(str2)))

deletionDistance(str1, str2) 
  -> deletionDistance(str1[a:], str2)
  -> deletionDistance(str1, str2[a:])

os
sa
O(m+n)
O(mn)
'''
deletion_distance('dog', 'frog')