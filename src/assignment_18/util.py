
from itertools import combinations

def iterator(pn, k):
    el = list(combinations(pn, k))
    count = 0
    for i in el:
        if any(item in i for item in pn[:k]):
            count += 1
    return round(count/len(el), 3)
