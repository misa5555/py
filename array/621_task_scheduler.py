class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        counter = Counter(tasks)
        window = n + 1
        biggest_freq = list(counter.values())[0]
        num_of_max_freq = list(counter.values()).count(biggest_freq)
        return window * (biggest_freq - 1) + num_of_max_freq
s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"], 2))
print(s.leastInterval(["A","A","A","B","B","B"], 0))
print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))