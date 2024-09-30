
def merge_the_tools(string, k):
    # your code goes here
    pp = len(string)//k
    wl = []
    result = []
    for i in range(pp):
        w = string[:k]
        wl.append(w)
        string = string[k:]
    for word in wl:
        word = list(word)
        el = []
        for i in word:
            if i not in el:
                el.append(i)
        nw = ''.join(el)
        result.append(nw)
    return result