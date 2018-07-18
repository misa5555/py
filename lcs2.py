from collections import defaultdict
def lcs(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return ""

    def createMapper(str):
        mapper = defaultdict(list)
        for i, element in enumerate(str):
            mapper[element].append(i)
        return mapper


    def search(str1, str2):
        mapper = createMapper(str2)
        originalMapper = createMapper(str2)
        lcsInStr2EndHere = -1
        result = ""
        for i in range(len(str1)):
            target = str1[i]
            if mapper.get(target):
                targetIdxInStr2 = mapper.get(target).pop(0)
                if targetIdxInStr2 < lcsInStr2EndHere:
                    lcsInStr2EndHere = targetIdxInStr2
                    mapper = originalMapper
                    mapper.get(target).pop(0)
                    result = target
                else:
                    lcsInStr2EndHere = targetIdxInStr2
                    result += target
        return result
    return search(str1, str2)
print(lcs("AGGTAB", "GXTXAYB"))
print(lcs("ABCDGH", "AEDFHR"))
print(lcs("thisisatest", "testing123testing"))
