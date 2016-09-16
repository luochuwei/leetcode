#pow(x,n)

def f(x, n):
	if n == 0:
		return 1
	v = f(x, n/2)
	if n%2 == 0:
		return v*v
	else:
		return v*v*x

def g(x, n):
	if n < 0:
		return 1.0/f(x, -n)
	else:
		return f(x,n)

print f(2,3)