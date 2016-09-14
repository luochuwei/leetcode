#Evaluate Reverse Polish Notation

def f(s):
    # s = list(s)
    operators = "+-*/"
    newstack = []
    for i in s:
        if i not in operators:
            newstack.append(i)
        else:
            a = int(newstack.pop())
            b = int(newstack.pop())
            if i == "+":
                newstack.append(a+b)
            elif i == "-":
                newstack.append(a-b)
            elif i == "*":
                newstack.append(a*b)
            elif i == "/":
                newstack.append(b/a)

    return int(newstack.pop())
    # return newstack


s = ["2", "1", "+", "3", "*"]
print f(s)
print f(["4", "13", "5", "/", "+"])