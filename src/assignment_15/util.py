
def no_idea(array, a, b):
    total = 0
    for i in array:
        if i in a:
            total += 1
        if i in b:
            total -= 1
    return total
