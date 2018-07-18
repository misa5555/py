import requests
import re
url = 'https://enigmatic-plains-7414.herokuapp.com/'

def download_file(url):
    local_filename = "instacart.txt"
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename
download_file(url)
with open('instacart.txt') as f:
    lines = f.readlines()
i = 0
ans = {}
while i < len(lines):
    idx = int(re.match(r'\d+', lines[i].strip()).group())
    lr = re.match(r'\[(\d+), (\d+)\]', lines[i+1].strip())
    x, y = int(lr.group(1)), int(lr.group(2))
    j = i + 2
    matrix = []
    while j < len(lines) and lines[j] != '\n':
        matrix = [lines[j]] + matrix
        j += 1
    target = matrix[y][x]
    ans[idx] = target
    i = j + 1

ans = sorted(ans.items(), key=lambda t: t[0])
print(ans)
pwd = ''
for el in ans:
    pwd += el[1]
print(pwd)


