#DI String Match
input = "IDID"
def diStringMatch(S):
    N = len(S)
    ni, nd = 0, N
    res = []
    for s in S:
        if s == "I":
            res.append(ni)
            ni += 1
        else:
            res.append(nd)
            nd -= 1
    res.append(ni)
    return res

print(diStringMatch(input))