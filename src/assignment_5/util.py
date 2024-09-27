
def str_format(n):
    res = []
    for i in range(1, n + 1):
        format_str = f"{i} {oct(i)[2:]} {hex(i)[2:]} {bin(i)[2:]}"
        res.append(format_str)
    return res
