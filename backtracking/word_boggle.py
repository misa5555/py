from collections import defaultdict
def wordBoggle(board, words):
    words = sorted(words)
    dp = defaultdict(list)
    ans = set()

    def dfs(word, visited, idx):
        if idx == len(word) - 1:
            ans.add(word)
            return True

        w = word[:idx + 1]
        vector = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for v in vector:
            i, j = visited[-1][0] + v[0], visited[-1][1] + v[1]
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and not (i, j) in set(visited) and board[i][j] == word[
                idx+1]:
                visited.append((i, j))
                dfs(word, visited, idx + 1)

    def get_start(ch):
        if dp.get(ch):
            return dp.get(ch)

        pos = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ch:
                    pos.append((i, j))
        dp[ch] = pos
        return dp.get(ch)

    for w in words:
        starts = get_start(w[0])
        for start in starts:
            dfs(w, [start], 0)
    return list(ans)

board = [
    ['R', 'L', 'D'],
    ['U', 'O', 'E'],
    ['C', 'S', 'O']
]
words = ["CODE", "SOLO", "RULES", "COOL"]
# print(wordBoggle(board, words))
b2 = [["G","T"],
 ["O","A"]]
w2 = ["TOGGLE", "GOAT", "TOO", "GO"]
# print(wordBoggle(b2, w2))

b3 = [["A","Q","A","H"],
 ["A","X","V","W"],
 ["A","L","T","I"],
 ["T","T","J","I"]]
w3 = ["AXOLOTL",
 "TAXA",
 "ABA",
 "VITA",
 "VITTA",
 "GO",
 "AXAL",
 "LATTE",
 "TALA"]
print(wordBoggle(b3, w3))