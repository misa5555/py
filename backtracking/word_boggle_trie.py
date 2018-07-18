def build_trie(words):
    trie = {}
    for w in words:
        tmp = trie
        for i, ch in enumerate(w):
            if ch not in tmp:
                tmp[ch] = {}
            tmp = tmp[ch]
        tmp['#'] = '#'
    return trie

def wordBoggle(board, words):
    trie = build_trie(words)
    vector = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    row, col = len(board), len(board[0])
    ans = []

    def dfs(pos, board, trie, path):
        i, j = pos
        if i < 0 or i >= row or j < 0 or j >= col or board[i][j] == '@' or board[i][j] not in trie:
            return
        ch = board[i][j]
        if trie.get(ch) and '#' in trie[ch]:
            ans.append(path + ch)

        board[i][j] = '@'
        for v in vector:
            dfs((pos[0] + v[0], pos[1] + v[1]), board, trie[ch], path + ch)
        board[i][j] = ch

    for i in range(row):
        for j in range(col):
            dfs((i, j), board, trie, '')

    return ans

board = [
    ['R', 'L', 'D'],
    ['U', 'O', 'E'],
    ['C', 'S', 'O']
]
print(wordBoggle(board, ["R", "CODE", "SOLO", "RULES", "COOL"]))

