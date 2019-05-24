#Assign Cookies

g = [1,2,3,4] #child
s = [1,2,3]  #cookies
# s >= g
def assignCookies(g,s):
    g.sort()
    s.sort()
    count = 0
    for i in range(len(g)):
        for j in range(len(s)):
            if s[j] >= g[i]:
                count += 1
                del s[j]
                break
    return count



print(assignCookies(g,s))


