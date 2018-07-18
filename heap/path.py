import re

def longestPath(fileSystem):
    start = fileSystem.find('\f')
    if start == -1:
        if '.' in fileSystem:
            return len(fileSystem)
        else:
            return 0

    dirs = [fileSystem[:start]]
    ans = []
    maxLen = 0
    i = start
    step = 0
    while i < len(fileSystem):
        matcher = re.match(r'(\f\t*)([^\n\t\f]*)', fileSystem[i:])
        if matcher:
            step = len(matcher.group(1)) - 1
            dirname = matcher.group(2)
            i += len(matcher.group())

        if len(dirs) >= step + 1:
            dirs[step] = dirname
        else:
            dirs.append(dirname)
        if '.' in dirname:
            maxLen = max(len('/'.join(dirs[:step+1])), maxLen)

    if '.' in dirs[-1]:
        maxLen = max(len('/'.join(dirs[:step+1])), maxLen)
    print(dirs)
    return maxLen


# print(longestPath("user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt"))
s2 = "user\f\tpictures\f\tdocuments\f\t\tnotes.txt"
# print(longestPath(s2))

# print(longestPath("dir\f    file.txt"))
print(longestPath("a\f\taa\f\t\taaa\f\t\t\tfile1234567890123.txt\faaaaaaaaaaaaaaaaaaaaa\f\tsth.png"))


def longestPath(fileSystem):
    maxlen = 0
    pathlen = {0:0}
    for line in fileSystem.splitlines():
        name = line.lstrip('\t')
        depth = len(line)-len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth]+len(name))
        else:
            pathlen[depth+1] = pathlen[depth] + len(name)+1
    return maxlen