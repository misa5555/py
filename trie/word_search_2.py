def findWords(board, words):
    trie = {}
    for w in words:
        t = trie
        for c in w:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['#'] = '#'
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            find(board, i, j, trie, '', res)
    return list(set(res))

def find(board, i, j, trie, path, res):
    if '#' in trie:
        res.append(path)
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in trie:
        return
    tmp = board[i][j]
    board[i][j] = "@"
    find(board, i+1, j, trie[tmp], path+tmp, res)
    find(board, i, j+1, trie[tmp], path+tmp, res)
    find(board, i-1, j, trie[tmp], path+tmp, res)
    find(board, i, j-1, trie[tmp], path+tmp, res)
    board[i][j] = tmp

words = ["oath","pea","eat","rain"]
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

findWords(board, words)