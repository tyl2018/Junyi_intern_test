def f(si):
    so = ""
    L = si.split()
    for string in L:
        s = ""
        for c in string:
            s = c + s
        so += s + " "
    return so[:-1]