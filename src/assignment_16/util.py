def word_order(l):
    s = set(l)
    nl = list(s)
    result = []
    for i in nl:
        result.append((i,l.count(i)))
    return result
