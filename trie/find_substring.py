# https://codefights.com/interview-practice/task/Ki9zRh5bfRhH6oBau
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        crt = self.root
        for ch in word:
            crt = crt.children[ch]
        crt.is_word = True

    def search(self, word):
        count = 0
        ans = -1
        crt = self.root
        for i, ch in enumerate(word):
            crt = crt.children.get(ch)
            if not crt:
                break
            count += 1
            if crt.is_word:
               ans = max(ans, count)
        return ans

def findSubstrings(words, parts):
    trie = Trie()
    for p in parts:
        trie.insert(p)
    print(trie.search("gurejkr"))
    def parse(w):
        maxStart = -1
        maxCount = -1
        for start in range(len(w)):
            count = trie.search(w[start:])
            if count and count > maxCount:
                maxStart = start
                maxCount = count
        # if maxStart > 0 and maxCount > 0:
        return w[:maxStart] + '[' + w[maxStart:maxStart + maxCount] + ']' + w[maxStart + maxCount:]
        # else:
        #     return w
    print(parse("grueire"))
    # result = []
    # for w in words:
    #     result.append(parse(w))
    # return result
words = ["Apple",
 "Melon",
 "Orange",
 "Watermelon"]
parts = ["a",
 "mel",
 "lon",
 "el",
 "An"]
# print(findSubstrings(words, parts))

words = ["neuroses",
 "myopic",
 "sufficient",
 "televise",
 "coccidiosis",
 "gules",
 "during",
 "construe",
 "establish",
 "ethyl"]
parts = ["aaaaa",
 "Aaaa",
 "E",
 "z",
 "Zzzzz",
 "a",
 "mel",
 "lon",
 "el",
 "An",
 "ise",
 "d",
 "g",
 "wnoVV",
 "i",
 "IUMc",
 "P",
 "KQ",
 "QfRz",
 "Xyj",
 "yiHS"]
print(findSubstrings(words, parts))

