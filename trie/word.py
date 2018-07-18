class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ch = words[0]
        for row in board:
            if ch in row:
                for cell in row:
                    if cell == ch:

