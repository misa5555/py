"""
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
"""
import copy;
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        columns = len(board[0])

        def nexts(pos, visited):
            i, j = pos
            nexts = []
            vectors = [(-1,0), (1,0), (0,-1),(0,1)]
            for v in vectors:
                if 0 <= i + v[0] < rows and 0 <= j + v[1] < columns and visited[i + v[0]][j + v[1]] == 0:
                    nexts.append((i + v[0], j + v[1]))
            return nexts
        def getChr(pos):
            return board[pos[0]][pos[1]]

        def search(word, start, visited):
            print(start)
            print(visited)
            if len(word) == 0:
                return True

            i, j = start
            if word[0] != board[i][j]:
                return False
            visited[i][j] = 1

            for n in nexts((i, j), visited):
                visited[i][j] = -1
                if search(word[1:], n, visited):
                    return True
                visited[i][j] = 1
            return False

        checker = list(map(set, board))
        visited = [[ 0 for _ in range(columns) ] for _ in range(rows)]
        return search(word, (0,0), visited)
        # starting_rows = []
        # for idx, row in enumerate(checker):
        #     if word[0] in row:
        #         starting_rows.append(idx)
        #
        # starts = []
        # for i in starting_rows:
        #     for j, cell in enumerate(board[i]):
        #         if board[i][j] == word[0]:
        #             starts.append((i,j))
        # original_board = copy.deepcopy(board)
        #
        # for start in starts:
        #     board = copy.deepcopy(original_board)
        #     visited = [[ 0 for _ in range(rows) ] for _ in range(columns)]
        #     search(word, visited)
        #
        # return False
s = Solution()
# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED"
# print(s.exist(board, word))
# board = [["a"]]
# word = "ab"
# print(s.exist(board, word))
# board = [
# ["C","A","A"],
# ["A","A","A"],
# ["B","C","D"]
# ]
# word = "AAB"
# print(s.exist(board, word))
board = [
["A","B","C","E"],
["S","F","E","S"],
["A","D","E","E"]]
word = "ABCESEEEFS"
print(s.exist(board, word))
board = [["a","a"]]
word = "aaa"
print(s.exist(board, word))
