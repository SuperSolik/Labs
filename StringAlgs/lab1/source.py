def prefix(string):
    res = [0]
    k = 0
    for i in range(1, len(string)):
        while k > 0 and string[i] != string[k]:
            k = res[k-1]
        if string[i] == string[k]:
            k += 1
        res.append(k)
    return res


def kmp(pattern, text):
    pref = prefix(pattern+'|'+text)
    res = []
    pl = len(pattern)
    tl = len(text)
    for i in range(pl+1, tl+pl+1):
        if pref[i] == pl:
            res.append(i - 2*pl)
    return res if res else [-1]


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(*kmp(str1, str2), end="")