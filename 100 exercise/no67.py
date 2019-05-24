#Valid Anagram
import collections

s = "anagram"
t = "nagaram"

check = True
def solution(s,t):
    s = collections.Counter(s)
    t = collections.Counter(t)
    if s ==t:
        return True
    else:
        return False

print(solution(s,t))
