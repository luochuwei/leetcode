#Isomorphic Strings
# if java, use hashmap
def f(s,t):
    if len(s) != len(t) or len(s) == 0 or len(t) == 0:
        return False
    d = {}

    for i in xrange(len(s)):
        c1 = s[i]
        c2 = t[i]
        if c1 in d:
            if d[c1] != c2:
                return False
        else:
            if c2 in d.values():
                return False
            d[c1] = c2

    return True


if f("egg", "add"):
    print "yes"