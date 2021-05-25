def f(si):
    so = ""
    L = si.split()
    for string in L:
        s = ""
        for c in string:
            s = c + s
        so += s + " "
    return so[:-1]

def test(si, so):
    if len(si) != len(so):
        print("Invalid")
        return False
    Li = si.split()
    Lo = so.split()
    for i in range(len(si)):
        if len(Li[s]) != len(Lo[s]):
            print("Invalid")
            return False
        for j in range(len(Li[s])):
            if Li[s][j] != Lo[s][-1-j]:
                print("Invalid")
                return False
    print("Valid")
    return True