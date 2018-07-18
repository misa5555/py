from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self, root):
        self.root = root

    def insert(self, word):
        crt = self.root
        for letter in word:
            crt = crt.children[letter]
        crt.is_word = True

    def search(self, word):
        crt = self.root
        for letter in word:
            crt = crt.children.get(letter)
            if not crt:
                return False
        return crt.is_word


class Solution:
    def findWords(self, board, words):
        """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
        root = TrieNode()
        trie = Trie(root)
        for w in words:
            trie.insert(w)

        row, col = len(board), len(board[0])
        result = []

        def dfs(pos, visited, crt, path):
            if crt.is_word:
                result.append(path)
            print(path)
            i, j = pos
            if i < 0 or i >= row or j < 0 or j >= col:
                return False
            if (i, j) in visited:
                return False
            crt = crt.children.get(board[i][j])
            if not crt:
                return False
            path += board[i][j]

            _visited = visited.add((i, j))
            dfs((i + 1, j), _visited, crt, path)
            dfs((i - 1, j), _visited, crt, path)
            dfs((i, j + 1), _visited, crt, path)
            dfs((i, j - 1), _visited, crt, path)

        crt = root
        for i in range(row):
            for j in range(col):
                dfs((i, j), set(), crt, "")
        return list(set(result))
