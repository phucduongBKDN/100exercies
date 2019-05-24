#Valid Parentheses
input = "()[]{}"
def solution(s):
    pars = [None]
    parmap = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in parmap:
            if parmap[c] != pars.pop():
                return False
        else:
            pars.append(c)
    return len(pars) == 1

print(solution(input))