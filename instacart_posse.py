import requests
import json
def len_check(a, b, c):
    uniqueness = len(set([len(a), len(b), len(c)]))
    return uniqueness == 1 or uniqueness == 3

def type_check(a, b, c):
    ch1 = {'u': 'u', 'Ü': 'u', 'ü': 'u', 'a': 'a', 'ä': 'a', 'Ä': 'a', 'Ö': 'o', 'ö': 'o', 'o': 'o', 'A': 'a', 'O': 'o', 'U': 'u'}
    uniqueness = len(set([ch1[a], ch1[b], ch1[c]]))
    return uniqueness == 1 or uniqueness == 3

def char_check(a, b, c):
    ch2 = {'a': 0, 'o': 0, 'u': 0, 'ä': 1, 'ü': 1, 'ö': 1, 'Ü': 2, 'Ä':2, 'Ö': 2, 'A': 3, 'O': 3, 'U': 3}
    uniqueness = len(set([ch2[a], ch2[b], ch2[c]]))
    return uniqueness == 1 or uniqueness == 3

def prefix_check(a, b, c):
    uniqueness = len(set([a, b, c]))
    return uniqueness == 1 or uniqueness == 3

def main_checker(ary):
    l = len(ary)
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if len_check(ary[i], ary[j], ary[k]) and type_check(ary[i][1], ary[j][1], ary[k][1]) and char_check(ary[i][1], ary[j][1], ary[k][1]) and prefix_check(ary[i][0], ary[j][0], ary[k][0]):
                    return (ary[i], ary[j], ary[k])

    return -1
def final_checker(ary):
    l = len(ary)
    ans = []
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if len_check(ary[i], ary[j], ary[k]) and type_check(ary[i][1], ary[j][1], ary[k][1]) and char_check(ary[i][1], ary[j][1], ary[k][1]) and prefix_check(ary[i][0], ary[j][0], ary[k][0]):
                    ans.append((ary[i], ary[j], ary[k]))
    return ans

def play():
    url = 'https://enigmatic-hamlet-4927.herokuapp.com/posse'
    r = requests.post(url)
    json_response = json.loads(r.text)
    id, board = json_response['id'], json_response['board']
    while True:
        print(board)
        ans = main_checker(board)
        print(ans)
        r2 = requests.post( url +'/' + id, data=json.dumps({'posse': ans}))
        res = json.loads(r2.text)
        if res.get('password'):
            break
        board = res['board']

    # requirement in the question 3) is not clear.
    # is this happening after the game is finished or during the game?
    r3 = requests.get(url +'/' + id)
    res = json.loads(r3.text)
    print(res)
    final_ans = final_checker(res['board'])
    print(final_ans)
play()

