#Print power set
#http://www.cnblogs.com/lovexjtu/archive/2011/06/15/2082234.html

def f(A):
    for i in xrange(pow(2,len(A))):
        tempNum = i
        pos = len(A) - 1
        while pos >= 0 and tempNum != 0:
            if tempNum & 1 != 0:
                print A[pos],
            tempNum = tempNum >> 1
            pos -= 1
        print

f([1,2,3])
