class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict
        from collections import Counter
        str_counter = set()
        for w in words:
            str_counter = str_counter.union(set(w))

        def compare(w1, w2):
            l = min(len(w1), len(w2))
            for i in range(l):
                if w1[i] != w2[i]:
                    return (w1[i], w2[i])
            return

        graph = defaultdict(list)
        for i in range(len(words) - 1):
            diff = compare(words[i], words[i+1])
            if diff:
                graph[diff[0]].append(diff[1])

        # caculating indegrees
        in_degrees = Counter()
        for key, values in graph.items():
            for dest in values:
                in_degrees[dest] += 1

        queue = []
        topo_order = []
        count = 0
        for ch in str_counter:
            if in_degrees[ch] == 0:
                queue.append(ch)

        while queue:
            target = queue.pop(0)
            topo_order.append(target)

            for ch in graph[target]:
                in_degrees[ch] -= 1
                if in_degrees[ch] == 0:
                    queue.append(ch)

            count += 1

        ans = ''.join(topo_order)
        print(ans)
        print(len(str_counter))
        print(count)
        if count == len(str_counter):
            return ans
        else:
            return ''


s = Solution()
words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

# s.alienOrder(words)
# s.alienOrder(["z", "x"])
# s.alienOrder(["z", "x", "z"])
s.alienOrder(["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"])