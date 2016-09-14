#Set Matrix Zeroes

def f(m):
    firstRow = 0
    firstColumn = 0

    for i in xrange(len(m)):
        if m[i][0] == 0:
            firstColumn = 1
            break
    for i in xrange(len(m[0])):
        if m[0][i] == 0:
            firstRow = 1
            break
    for i in xrange(len(m)):
        for j in xrange(len(m[0])):
            if m[i][j] == 0:
                m[i][0] = 0
                m[0][j] = 0
    for i in xrange(len(m)):
        for j in xrange(len(m[0])):
            if m[i][0] == 0 or m[0][j] == 0:
                m[i][j] = 0

    if firstRow:
        for i in xrange(len(m[0])):
            m[0][i] = 0

    if firstColumn:
        for i in xrange(len(m)):
            m[i][0] = 0
    return m

print f([[1,1,1,0],
         [1,1,0,0],
         [1,1,0,0],
         [1,0,0,0]])