#Rotate Array
"""
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. 
"""

def f(list_a, k):
    for i in xrange(k):
        for j in xrange(len(list_a)-1, 0, -1):
            temp = list_a[j]
            list_a[j] = list_a[j-1]
            list_a[j-1] = temp
    return list_a


def reverse(list_a, i, j):
    while i < j:
        temp = list_a[i]
        list_a[i] = list_a[j]
        list_a[j] = temp
        i += 1
        j -= 1

def f2(list_a, k):
    """
    1. Divide the array two parts: 1,2,3,4 and 5, 6
    2. Reverse first part: 4,3,2,1,5,6
    3. Reverse second part: 4,3,2,1,6,5
    4. Reverse the whole array: 5,6,1,2,3,4
    """
    reverse(list_a, 0, len(list_a)-k-1)
    reverse(list_a, len(list_a)-k, len(list_a)-1)
    reverse(list_a, 0, len(list_a)-1)
    return list_a

print f(range(7), 3)
print f2(range(7), 3)