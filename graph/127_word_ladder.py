class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import defaultdict
        graph = defaultdict(list)

        def is_adjacent(w1, w2):
            count = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    count += 1
                    if count > 1:
                        return False
            return count == 1
        print(is_adjacent('leet', 'lest'))

        def build_tree(wordList):
            tmp = [beginWord] + wordList
            for i in range(len(tmp)):
                for j in range(len(tmp)):
                    w1, w2 = tmp[i], tmp[j]
                    if is_adjacent(w1, w2) == True:
                        graph[w1].append(w2)
            return graph

        # graph = build_tree(wordList)
        # visited = set()
        # queue = [(beginWord, 1)]
        # while queue:
        #     crt = queue.pop(0)
        #     crt_node, count = crt[0], crt[1]
        #     if crt_node == endWord:
        #         return count
        #     visited.add(crt_node)
        #     neighbours = graph.get(crt_node)
        #     if neighbours:
        #         new_elements = [ (n, count + 1) for n in neighbours if n not in visited ]
        #         queue += new_elements
        # return -1

s = Solution()
s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])