#Reverse Words in a String

def reverse(list_a, i, j):
    """字符逆序"""
    while i <= j:
        temp = list_a[i]
        list_a[i] = list_a[j]
        list_a[j] = temp
        i += 1
        j -= 1

def reverseWords(list_a):
    last = 0

    for j in xrange(len(list_a)):
        if list_a[j] == ' ':
            reverse(list_a, last, j-1)
            last = j + 1

    reverse(list_a, last, len(s)-1) #颠倒最后一个词
    reverse(list_a, 0, len(s)-1) #颠倒整句话
    return list_a

s = "the sky is blue"
print s
s_ = reverseWords(list(s))
ans = ''
for i in s_:
    ans += i
print ans