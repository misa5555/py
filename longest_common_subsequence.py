from collections import defaultdict
def lcs(str1, str2):
    def createMapper(str):
        mapper = defaultdict(list)
        for i, element in enumerate(str):
            mapper[element].append(i)
        return mapper


    tracer1 = [0] * len(str1)
    tracer2 = [0] * len(str2)
    mapper = createMapper(str2)
    print(mapper)
    options = []
    def search(idx1, idx2, str1, str2, result):
        if idx1 == len(str1) - 1 or idx2 == len(str2) - 1:
            return result

        # assume str1 is always shorter than str2
        for i in range(idx1, len(str1)):
            if tracer1[i] == 0:
                target = str1[i]
                #print(target)
                # iterate through all the index valuds of target in str2
                for j in mapper[target]:
                    if j >= idx2 and tracer2[j] == 0:
                        print("match!")
                        result += target
                        tracer1[i] = 1
                        tracer2[j] = 1
                        if i <= len(str1) - 2 and j <= len(str2) - 2:
                            search(i + 1, j + 1, str1, str2, result)
    return search(0, 0, str1, str2, "")
print(lcs("AGGTAB", "GXTXAYB"))
